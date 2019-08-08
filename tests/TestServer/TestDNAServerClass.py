from unittest import TestCase
import random
from dnac_api.Server import RequestHandler, DNAServer


class ControlledRequestHandler(RequestHandler):

    def __init__(self):
        self.get_params_passed = {}
        self.get_kwargs_passed = {}
        self.get_url_passed = {}

    def get(self, url, params=None, **kwargs):
        id = random.randint(1, 9999999999999999999)
        self.get_params_passed[id] = params
        self.get_kwargs_passed[id] = kwargs
        self.get_url_passed[id] = url
        return id

    def post(self, url, data, json=None, **kwargs):
        pass

    def put(self, url, data, **kwargs):
        pass

    def delete(self, url, **kwargs):
        pass

    def request(self, method, url, **kwargs):
        class ReturnObj:
            def json(self):
                return {'Token': 'JunkToken'}
        return ReturnObj()


class TestableDNAServer(DNAServer, ControlledRequestHandler):
    '''
    Inject the ControlledRequestHandler dependancy in front of the RequestHandler class so we can Isolate
    the DNAServer class and test it. This object allows us test the code in the DNAServer class while controlling
    what data is sent and received instead of it using the RequestHandler class in the project.
    '''
    def __init__(self, *args, **kwargs):
        DNAServer.__init__(self, *args, **kwargs)
        ControlledRequestHandler.__init__(self)


class TestInstantiation(TestCase):

    def test_token_stored_on_instantiation(self):
        instance = TestableDNAServer('host', 'user', 'pass')
        self.assertEqual(instance.session_token, 'JunkToken')


class TestGetHandler(TestCase):

    def setUp(self) -> None:
        self.instance = TestableDNAServer('host', 'user', 'password')

    def test_passes_custom_headers_properly(self):
        id = self.instance.get_handler('dummy_url', custom_headers={'CustomValue': 'Junk'})
        self.assertEqual(self.instance.get_kwargs_passed[id]['headers']['CustomValue'], 'Junk')

    def test_passes_params_properly(self):
        id = self.instance.get_handler('dummy_url', params={'JunkParam': 'Junk'})
        self.assertEqual(self.instance.get_params_passed[id]['JunkParam'], 'Junk')

    def test_includes_token_in_header(self):
        id = self.instance.get_handler('dummy_url')
        self.assertEqual(self.instance.get_kwargs_passed[id]['headers']['x-auth-token'], 'JunkToken')

    def test_passes_url(self):
        id = self.instance.get_handler('/my/url')
        self.assertEqual(self.instance.get_url_passed[id], 'https://host/api/v1/my/url')