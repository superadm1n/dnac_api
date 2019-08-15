from dnac_api.v1_1.v1_1_Server import DNAServer
from tests.controlled_objects import ControlledRequestHandler
from unittest import TestCase


class TestableDNAServer(DNAServer, ControlledRequestHandler):
    '''
    Inject the ControlledRequestHandler dependancy in front of the RequestHandler class so we can Isolate
    the DNAServer class and test it. This object allows us test the code in the DNAServer class while controlling
    what data is sent and received instead of it using the RequestHandler class in the project.
    '''
    def __init__(self, *args, **kwargs):
        DNAServer.__init__(self, *args, **kwargs)
        ControlledRequestHandler.__init__(self)


class TestV1_1DnaServer(TestCase):

    def setUp(self) -> None:
        self.instance = TestableDNAServer('host', 'user', 'pass')
        self.execution_id = self.instance.get('')

    def test_passes_correct_base_url(self):
        self.assertEqual('https://host/api/v1', self.instance.base_url)