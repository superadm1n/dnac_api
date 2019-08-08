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
import requests
from requests.auth import HTTPBasicAuth


class RequestHandler:

    def request(self, method, url, **kwargs):
        return requests.request(method, url, **kwargs)

    def get(self, url, params=None, **kwargs):
        return requests.get(url, params, **kwargs)

    def post(self, url, data, json=None, **kwargs):
        return requests.post(url, data, json, **kwargs)

    def put(self, url, data, **kwargs):
        return requests.put(url, data, **kwargs)

    def delete(self, url, **kwargs):
        return requests.delete(url, **kwargs)


class DNAServer(RequestHandler):

    def __init__(self, dna_server, username, password, verify=False):
        self.dna_server = dna_server
        self.username = username
        self.password = password
        self.verify = verify
        self.base_url = 'https://{}/api/v1'.format(self.dna_server)

        self.session_token = self._login()

    def _login(self):
        url = "https://{}/api/system/v1/auth/token".format(self.dna_server)
        response = self.request("POST", url, auth=HTTPBasicAuth(self.username, self.password), verify=False)
        return response.json()["Token"]

    def get_handler(self, url, custom_headers=None, params=None):
        headers = {}
        string_paramenters = {}
        if custom_headers:
            for key, value in custom_headers.items():
                headers[key] = value
        if params:
            for key, value in params.items():
                string_paramenters[key] = value

        headers["x-auth-token"] = self.session_token
        response = self.get('{}{}'.format(self.base_url, url), headers=headers, params=string_paramenters, verify=self.verify)
        return response

    def post_handler(self, url, data, custom_headers=None):
        headers = {}
        if custom_headers:
            for key, value in custom_headers.items():
                headers[key] = value
        headers["x-auth-token"] = self.session_token

        return self.post('{}{}'.format(self.base_url, url), data=data, headers=headers)

    def response_handler(self, response):
        return response.json()['response']
