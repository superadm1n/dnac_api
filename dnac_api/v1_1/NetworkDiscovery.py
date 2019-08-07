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

from dnac_api.Server import DNAServer


class GlobalCredentials(DNAServer):

    # TODO: add setters to update the values on the server. setters should handle both posts and puts depending on the data passed into the value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = '{}/global-credential'.format(self.base_url)

    def credential_sub_type(self, credential_id):
        '''Returns the credential Sub Type given the ID of a credential'''
        url = '{}/{}'.format(self.url, credential_id)
        response = self.get_handler(url)
        return self.response_handler(response)

    @property
    def cli(self):
        headers = {'credentialSubType': 'CLI'}
        response = self.get_handler(self.url, params=headers)
        return self.response_handler(response)

    @property
    def snmpv2_read(self):
        headers = {'credentialSubType': 'SNMPV2_READ_COMMUNITY'}
        response = self.get_handler(self.url, params=headers)
        return self.response_handler(response)

    @property
    def snmpv2_write(self):
        headers = {'credentialSubType': 'SNMPV2_WRITE_COMMUNITY'}
        response = self.get_handler(self.url, params=headers)
        return self.response_handler(response)

    @property
    def snmpv3(self):
        headers = {'credentialSubType': 'SNMPV3'}
        response = self.get_handler(self.url, params=headers)
        return self.response_handler(response)

    @property
    def http_write(self):
        headers = {'credentialSubType': 'HTTP_WRITE'}
        response = self.get_handler(self.url, params=headers)
        return self.response_handler(response)

    @property
    def http_read(self):
        headers = {'credentialSubType': 'HTTP_READ'}
        response = self.get_handler(self.url, params=headers)
        return self.response_handler(response)

    @property
    def netconf(self):
        headers = {'credentialSubType': 'NETCONF'}
        response = self.get_handler(self.url, params=headers)
        return self.response_handler(response)


class Discoveries(DNAServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def number_of_discoveries(self):
        url = '{}/discovery/count'.format(self.base_url)
        return self.get_handler(url).json()['response']

    def discovery_by_id(self, id):
        '''Untested'''
        url = '{}/discovery/{}'.format(self.base_url, id)
        return self.response_handler(self.get_handler(url))

    def discovery_jobs_for_ip(self, ip):
        '''Untested'''
        url = '{}/discovery/job'.format(self.base_url)
        response = self.get_handler(url, params={'ipAddress': ip})
        return self.response_handler(response)

    def physical_topology(self):
        url = '{}/topology/physical-topology'.format(self.base_url)
        return self.get_handler(url)


class API(GlobalCredentials, Discoveries):
    pass