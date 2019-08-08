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
    """
    This class is a wrapper for the requests api. It buys us the ability in the future to utilize a different
    package to handle the requests if it is decided. It also allows us to test the DNAServer class via
    dependency injection
    """

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
    """
    This class handles interfacing the api level of the package with the handling of the requests to the DNA server.
    It provides a standard way for the rest of the package to send data to the DNA Center server.
    """

    def __init__(self, dna_server, username, password, verify=False):
        self.dna_server = dna_server
        self.username = username
        self.password = password
        self.verify = verify
        self.base_url = 'https://{}/api/v1'.format(self.dna_server)

        self.session_token = self._login()

    def _login(self):
        """Logs into the DNA Center server, returning the token that can be used for all subsequent
        requests in the session

        :return:
        """
        url = "https://{}/api/system/v1/auth/token".format(self.dna_server)
        response = self.request("POST", url, auth=HTTPBasicAuth(self.username, self.password), verify=False)
        return response.json()["Token"]

    def get_handler(self, url, custom_headers=None, params=None):
        """Handles sending a get request to the DNA Center Server

        :param url: Relative URL location of the DNA Center REST API ex. /discovery/count
        :type url: str
        :param custom_headers: Custom headers to send in the get request
        :type custom_headers: dict
        :param params: Custom URL parameters to send in the get request
        :type params: dict
        :return: raw response from the DNAC server. Currently passes up the object that is given from the requests package
        """
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
        """Handles sending a post request to the DNA Center Server

        :param url: Relative URL location of the DNA Center REST API ex. /discover/count
        :type url: str
        :param data: Data to send along with the post request
        :param custom_headers: Custom headers to send in the post reqeuest
        :type custom_headers:dict
        :return:
        """
        headers = {}
        if custom_headers:
            for key, value in custom_headers.items():
                headers[key] = value
        headers["x-auth-token"] = self.session_token

        return self.post('{}{}'.format(self.base_url, url), data=data, headers=headers)

    def response_handler(self, response):
        """Extracts the data that was sent back from the server. Not sure if I will keep this in as it
        depends on the requests library and I might add extra pre processing of the data returned from the server.

        :param response:
        :return:
        """
        return response.json()['response']
