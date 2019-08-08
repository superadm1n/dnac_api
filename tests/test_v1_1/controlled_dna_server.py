from random import randint
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
        id = randint(1, 99999999999)
        self.get_handler_passed_url[id] = url
        self.get_handler_passed_headers[id] = custom_headers
        self.get_handler_passed_url_paramenters[id] = params
        return id

    def post_handler(self, url, data, custom_headers=None):
        id = randint(1, 99999999999)
        self.post_handler_passed_url[id] = url
        self.post_handler_passed_headers[id] = custom_headers
        self.post_handler_passed_data[id] = data
        return id

    def response_handler(self, response):
        self.response_handler_called += 1
        return response
