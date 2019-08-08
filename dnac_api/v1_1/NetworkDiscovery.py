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
from dnac_api.lib.kwarg_hander import handle_kwargs


class GlobalCredentials(DNAServer):

    # TODO: add setters to update the values on the server. setters should handle both posts and puts depending on the data passed into the value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = '/global-credential'
        self.allowed_kwargs = ['credentialSubType', 'sortBy', 'order']

    def credential_sub_type(self, credential_id):
        '''Returns the credential Sub Type given the ID of a credential'''
        url = '{}/{}'.format(self.url, credential_id)
        response = self.get_handler(url)
        return self.response_handler(response)

    def cli(self, **kwargs):
        url_params = {'credentialSubType': 'CLI'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def snmpv2_read(self, **kwargs):
        url_params = {'credentialSubType': 'SNMPV2_READ_COMMUNITY'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def snmpv2_write(self, **kwargs):
        url_params = {'credentialSubType': 'SNMPV2_WRITE_COMMUNITY'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def snmpv3(self, **kwargs):
        url_params = {'credentialSubType': 'SNMPV3'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def http_write(self, **kwargs):
        url_params = {'credentialSubType': 'HTTP_WRITE'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def http_read(self, **kwargs):
        url_params = {'credentialSubType': 'HTTP_READ'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def netconf(self, **kwargs):
        url_params = {'credentialSubType': 'NETCONF'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)


class Discoveries(DNAServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def number_of_discoveries(self):
        url = '/discovery/count'
        return self.get_handler(url).json()['response']

    def discovery_by_id(self, discovery_id):
        '''Untested'''
        url = '/discovery/{}'.format(discovery_id)
        return self.response_handler(self.get_handler(url))

    def discovery_jobs_by_id(self, discovery_id, **kwargs):
        allowed_kwargs = ['offset', 'limit', 'ipAddress']
        url = '/discover/{}/job'.format(discovery_id)
        url_params = handle_kwargs(params={}, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=url_params if url_params else None))

    def network_devices_from_discovery_by_filters(self, discovery_id, **kwargs):
        allowed_kwargs = ['taskId', 'sortyBy', 'sortOrder', 'ipAddress', 'pingStatus', 'snmpStatus', 'cliStatus', 'netconfStatus', 'httpStatus']
        url = '/discovery/{}/summary'.format(discovery_id)
        url_params = handle_kwargs(params={}, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=url_params if url_params else None))

    def discovery_jobs_for_ip(self, ip, **kwargs):
        '''Untested'''
        allowed_kwargs = ['offset', 'limit', 'name']
        url = '/discovery/job'
        url_params = {'ipAddress': ip}
        # append additional paramenters
        url_params = handle_kwargs(url_params, allowed_kwargs=allowed_kwargs, **kwargs)

        response = self.get_handler(url, params=url_params)
        return self.response_handler(response)

    def num_network_devices_in_discovery(self, discovery_id):
        url = '/discovery/{}/network-device/count'.format(discovery_id)
        return self.response_handler(self.get_handler(url))

    def physical_topology(self):
        url = '/topology/physical-topology'
        return self.get_handler(url)


class API(GlobalCredentials, Discoveries):
    pass