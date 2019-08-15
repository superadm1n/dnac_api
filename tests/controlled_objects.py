import random
from dnac_api.RequestHandler import ResponseObject, RequestHandler
from dnac_api.Server import DNAServer


class ControlledDNAServer(DNAServer):
    """
    Child class of the DNAServer which over rides the methods allowing us to see and validate how higher
    classes are interacting with the DNA server
    """

    def __init__(self):
        self.response_handler_called = 0

        self.get_handler_passed_url = {}
        self.get_handler_passed_headers = {}
        self.get_handler_passed_url_paramenters = {}

        self.post_handler_passed_url = {}
        self.post_handler_passed_headers = {}
        self.post_handler_passed_data = {}

    def get_handler(self, url, custom_headers=None, params=None):
        id = random.randint(1, 99999999999)
        self.get_handler_passed_url[id] = url
        self.get_handler_passed_headers[id] = custom_headers
        self.get_handler_passed_url_paramenters[id] = params
        return id

    def post_handler(self, url, data, custom_headers=None):
        id = random.randint(1, 99999999999)
        self.post_handler_passed_url[id] = url
        self.post_handler_passed_headers[id] = custom_headers
        self.post_handler_passed_data[id] = data
        return id

    def response_handler(self, response):
        self.response_handler_called += 1
        return response


class ControlledRequestHandler(RequestHandler):

    def __init__(self):
        self.get_params_passed = {}
        self.get_kwargs_passed = {}
        self.get_url_passed = {}

        self.post_url_passed = {}
        self.post_data_passed = {}
        self.post_json_passed = {}
        self.post_kwargs_passed = {}

        self.put_url_passed = {}
        self.put_data_passed = {}
        self.put_kwargs_passed = {}

    def get(self, url, params=None, **kwargs):
        id = random.randint(1, 9999999999999999999)
        self.get_params_passed[id] = params
        self.get_kwargs_passed[id] = kwargs
        self.get_url_passed[id] = url
        return id

    def post(self, url, data, json=None, **kwargs):
        id = random.randint(1, 9999999999999999999)
        self.post_url_passed[id] = url
        self.post_data_passed[id] = data
        self.post_json_passed[id] = json
        self.post_kwargs_passed[id] = kwargs
        return id

    def put(self, url, data, **kwargs):
        id = random.randint(1, 9999999999999999999)
        self.put_url_passed[id] = url
        self.put_data_passed[id] = data
        self.put_kwargs_passed[id] = kwargs
        return id

    def delete(self, url, **kwargs):
        pass

    def request(self, method, url, **kwargs):
        return ResponseObject(response_data={'Token': 'JunkToken'}, status_code=200)
