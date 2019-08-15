"""
dnac-api is Python implementation of an SDK for the Cisco DNA Center REST API

Copyright (C) 2019  Kyle Kowalczyk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from unittest import TestCase
from dnac_api.Server import DNAServer
from tests.controlled_objects import ControlledRequestHandler
from dnac_api.RequestHandler import ResponseObject


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


class TestPostHandler(TestCase):
    def setUp(self) -> None:
        self.instance = TestableDNAServer('host', 'user', 'password')

    def test_passes_url_properly(self):
        id = self.instance.post_handler('/my/url', data='Junk')
        self.assertEqual(self.instance.post_url_passed[id], 'https://host/api/v1/my/url')

    def test_passes_data_properly(self):
        id = self.instance.post_handler('/my/url', data='Junk')
        self.assertEqual('"Junk"', self.instance.post_data_passed[id])

    def test_includes_token_in_header(self):
        id = self.instance.post_handler('/my/url', data='Junk')
        self.assertEqual(self.instance.post_kwargs_passed[id]['headers']['x-auth-token'], 'JunkToken')

    def test_passes_custom_headers_properly(self):
        id = self.instance.post_handler('/my/url', data='Junk', custom_headers={'HeaderKey': 'HeaderValue'})
        self.assertEqual(self.instance.post_kwargs_passed[id]['headers']['HeaderKey'], 'HeaderValue')


class TestResponseHandler(TestCase):
    def setUp(self) -> None:
        self.instance = TestableDNAServer('host', 'user', 'password')

    def test_basic_test(self):
        return_obj = ResponseObject(status_code=200, response_data='JunkResponse')
        self.assertEqual('JunkResponse', self.instance.response_handler(return_obj))


class TestPutHandler(TestCase):
    def setUp(self) -> None:
        self.instance = TestableDNAServer('host', 'user', 'password')

    def test_passes_url_properly(self):
        id = self.instance.put_handler('/my/url', data='Junk')
        self.assertEqual(self.instance.put_url_passed[id], 'https://host/api/v1/my/url')

    def test_passes_data_properly(self):
        id = self.instance.put_handler('/my/url', data='Junk')
        self.assertEqual('Junk', self.instance.put_data_passed[id])

    def test_includes_token_in_header(self):
        id = self.instance.put_handler('/my/url', data='Junk')
        self.assertEqual(self.instance.put_kwargs_passed[id]['headers']['x-auth-token'], 'JunkToken')

    def test_passes_custom_headers_properly(self):
        id = self.instance.put_handler('/my/url', data='Junk', custom_headers={'HeaderKey': 'HeaderValue'})
        self.assertEqual(self.instance.put_kwargs_passed[id]['headers']['HeaderKey'], 'HeaderValue')
