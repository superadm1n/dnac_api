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
import json


class GlobalCredentials(DNAServer):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = '/global-credential'
        self.allowed_kwargs = ['credentialSubType', 'sortBy', 'order']

    def credential_sub_type(self, credential_id):
        '''This method is used to get global credential for the given credential sub type

        :param credential_id: Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF
        :return:
        '''
        url = '{}/{}'.format(self.url, credential_id)
        response = self.get_handler(url)
        return self.response_handler(response)

    def cli(self, **kwargs):
        """This method is used to get global CLI credentials. This method gets to
        the api route ``/global-credential``

        :param kwargs: See Keyword Arguments below for available keyword arguments.
        :Keyword Arguments:
            * *sortBy* (``str``) -- define sorting on the data returned
            * *order* (``str``) -- Define order on data returned
        :return: Global CLI Credentials
        """
        url_params = {'credentialSubType': 'CLI'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def create_cli_credentials(self, username, password, enable_password, comments,  description):
        """Sends POST request to ``/global-credential/cli`` to create new cli credential entry.

        :param username: Username used in the credentials
        :param password: Password used in the credentials
        :param enable_password: Enable password used in the credentials
        :param comments: Brief Comment
        :param description: Brief Description
        :return:
        """
        data = {'username': username, 'password': password, 'enablePassword': enable_password, 'comments': comments, 'description': description}
        return self.post_handler('/global-credential/cli', data=[data])

    def snmpv2_read(self, **kwargs):
        """This method is used to get global SNMPv2 Read credentials. This method gets to
        the api route ``/global-credential``

        :param kwargs: See Keyword Arguments below for available keyword arguments.
        :Keyword Arguments:
            * *sortBy* (``str``) -- define sorting on the data returned
            * *order* (``str``) -- Define order on data returned
        :return: Global SNMPv2 Read Credentials
        """
        url_params = {'credentialSubType': 'SNMPV2_READ_COMMUNITY'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def create_snmpv2_read(self, community_string, comments, description):
        """Creates new SNMPv2 Read credentials by submitting a post request to ``/global-credential/snmpv2-read-community``

        :param community_string: Community string
        :type community_string: str
        :param comments: Comments
        :type comments: str
        :param description: Descriptiomn
        :type description: str
        :return:
        """
        data = {"readCommunity": community_string, "comments": comments, "description": description}
        return self.post_handler('/global-credential/snmpv2-read-community', data=[data])

    def snmpv2_write(self, **kwargs):
        """This method is used to get global SNMPv2 Write credentials. This method gets to
        the api route ``/global-credential``

        :param kwargs: See Keyword Arguments below for available keyword arguments.
        :Keyword Arguments:
            * *sortBy* (``str``) -- define sorting on the data returned
            * *order* (``str``) -- Define order on data returned
        :return: Global SNMPv2 Write Credentials
        """
        url_params = {'credentialSubType': 'SNMPV2_WRITE_COMMUNITY'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def create_snmpv2_write(self, community_string, comments, description):
        """Creates new SNMPv2 Write credentials by submitting a post request to ``/global-credential/snmpv2-write-community``

        :param community_string: Community string
        :type community_string: str
        :param comments: Comments
        :type comments: str
        :param description: Descriptiomn
        :type description: str
        :return:
        """
        data = {"writeCommunity": community_string, "comments": comments, "description": description}
        return self.post_handler('/global-credential/snmpv2-write-community', data=[data])

    def snmpv3(self, **kwargs):
        """This method is used to get global SNMPv3 credentials. This method gets to
        the api route ``/global-credential``

        :param kwargs: See Keyword Arguments below for available keyword arguments.
        :Keyword Arguments:
            * *sortBy* (``str``) -- define sorting on the data returned
            * *order* (``str``) -- Define order on data returned
        :return: Global SNMPv3 Credentials
        """
        url_params = {'credentialSubType': 'SNMPV3'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def create_snmpv3_credentials(self, privacy_password, privacy_type, snmp_mode, auth_type, auth_password, username, comments, description):
        """Creates new SNMPv3 credentials by submitting a post request to ``/global-credential/snmpv3``

        :param privacy_password:
        :param privacy_type:
        :param snmp_mode:
        :param auth_type:
        :param auth_password:
        :param username:
        :param comments:
        :param description:
        :return:
        """
        data = {"privacyPassword": privacy_password, "privacyType": privacy_type, "snmpMode": snmp_mode, "authType":auth_type,
                "authPassword": auth_password, "username": username, "comments": comments,  "description": description}

        return self.post_handler('/global-credential/snmpv3', data=[data])

    def http_write(self, **kwargs):
        """This method is used to get global HTTP Write credentials. This method gets to
        the api route ``/global-credential``

        :param kwargs: See Keyword Arguments below for available keyword arguments.
        :Keyword Arguments:
            * *sortBy* (``str``) -- define sorting on the data returned
            * *order* (``str``) -- Define order on data returned
        :return: Global HTTP Write Credentials
        """
        url_params = {'credentialSubType': 'HTTP_WRITE'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def create_http_write_credentials(self, username, password, port, secure, comments, description):
        """Creates new HTTP Write credentials by submitting a post request to ``/global-credential/http-write``

        :param username:
        :type username: str
        :param password:
        :type password: str
        :param port:
        :type port: int
        :param secure:
        :type secure: bool
        :param comments:
        :type comments: str
        :param description:
        :type description: str
        :return:
        :rtype: ResponseObject
        """
        data = {"port": port, "secure": secure, "username": username, "password": password, "comments": comments,
                "description": description}
        return self.post_handler('/global-credential/http-write', data=[data])


    def http_read(self, **kwargs):
        """This method is used to get global HTTP Read credentials. This method gets to
        the api route ``/global-credential``

        :param kwargs: See Keyword Arguments below for available keyword arguments.
        :Keyword Arguments:
            * *sortBy* (``str``) -- define sorting on the data returned
            * *order* (``str``) -- Define order on data returned
        :return: Global HTTP Read Credentials
        """
        url_params = {'credentialSubType': 'HTTP_READ'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def create_http_read_credentials(self, username, password, port, secure, comments, description):
        """Creates new HTTP Read credentials by submitting a post request to ``/global-credential/http-read``

        :param username:
        :type username: str
        :param password:
        :type password: str
        :param port:
        :type port: int
        :param secure:
        :type secure: bool
        :param comments:
        :type comments: str
        :param description:
        :type description: str
        :return:
        :rtype: ResponseObject
        """
        data = {"port": port, "secure": secure, "username": username, "password": password, "comments": comments,
                "description": description}
        return self.post_handler('/global-credential/http-read', data=[data])

    def netconf(self, **kwargs):
        """This method is used to get global Netconf credentials. This method gets to
        the api route ``/global-credential``

        :param kwargs: See Keyword Arguments below for available keyword arguments.
        :Keyword Arguments:
            * *sortBy* (``str``) -- define sorting on the data returned
            * *order* (``str``) -- Define order on data returned
        :return: Global Netconf Credentials
        """
        url_params = {'credentialSubType': 'NETCONF'}
        url_params = handle_kwargs(url_params, self.allowed_kwargs, **kwargs)
        response = self.get_handler(self.url, params=url_params)
        return self.response_handler(response)

    def create_netconf_credentials(self, netconf_port, comments, description):
        """Creates new netconf credentials by submitting a post request to ``/global-credential/netconf``

        :param netconf_port:
        :param comments:
        :param description:
        :return:
        """
        data = {"netconfPort": netconf_port, "comments": comments, "description": description}
        return self.post_handler('/global-credential/netconf', data=[data])


class Discoveries(DNAServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def number_of_discoveries(self):
        url = '/discovery/count'
        return self.response_handler(self.get_handler(url))

    def start_discovery_process(self, **kwargs):
        """Initiates discovery with the given parameters

        :param kwargs: See Keyword Arguments below
        :Keyword Arguments:

            * *snmpMode* (``str``)
            * *netconfPort* (``str``)
            * *preferredMgmtIPMethod* (``str``)
            * *name* (``str``)
            * *globalCredentialIdList*  (``list(str)``)
            * *httpReadCredential*: (``dict``)
                * *port* (``integer``)
                * *secure* (``boolean``)
                * *username* (``string``)
                * *password* (``string``)
                * *comments* (``string``)
                * *credentialType* (``string``)
                * *description* (``string``)
                * *id* (``string``)
                * *instanceUuid* (``string``)



            * *httpWriteCredential*: (``dict``)
                * *port* (``integer``)
                * *secure* (``boolean``)
                * *username* (``string``)
                * *password* (``string``)
                * *comments* (``string``)
                * *credentialType* (``string``)
                * *description* (``string"``)
                * *id* (``string"``)
                * *instanceUuid* (``string``)


            * *parentDiscoveryId* (``str``)
            * *snmpROCommunityDesc* (``str``)
            * *snmpRWCommunityDesc* (``str``)
            * *snmpUserName* (``str``)
            * *timeout* (``int``)
            * *snmpVersion* (``str``)
            * *ipAddressList* (``str``)
            * *cdpLevel* (``int``)
            * *enablePasswordList*: (``list(string)``)
            * *ipFilterList*: (``list(string)``)
            * *passwordList*: (``list(string)``)
            * *protocolOrder* (``str``)
            * *reDiscovery* (``bool``)
            * *retry* (``int``)
            * *snmpAuthPassphrase* (``str``)
            * *snmpAuthProtocol* (``str``)
            * *snmpPrivPassphrase* (``str``)
            * *snmpPrivProtocol* (``str``)
            * *snmpROCommunity* (``str``)
            * *snmpRWCommunity* (``str``)
            * *userNameList* (``list(string)``)
            * *discoveryType* (``str``)

        :return:
        """
        url = '/discovery'
        self.post_handler(url, kwargs)

    def discovery_by_id(self, discovery_id):
        """Gets discovery by specified ID, sends a GET request to ``/discovery/{id}``

        :param discovery_id:
        :return:
        """
        url = '/discovery/{}'.format(discovery_id)
        return self.response_handler(self.get_handler(url))

    def discovery_jobs_by_id(self, discovery_id, **kwargs):
        """Returns discovery jobs by specified ID.

        :param discovery_id:
        :param kwargs: See Keyword Arguments below
        :Keyword Arguments:
            * *offset* (``str``)
            * *limit* (``str``)
            * *ipAddress* (``str``)
        :return:
        """
        allowed_kwargs = ['offset', 'limit', 'ipAddress']
        url = '/discovery/{}/job'.format(discovery_id)
        url_params = handle_kwargs(params={}, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=url_params if url_params else None))

    def network_devices_from_discovery_by_filters(self, discovery_id, **kwargs):
        """

        :param discovery_id:
        :param kwargs: See Keyword Arguments below
        :Keyword Arguments:
            * *offset* (``str``)
            * *limit* (``str``)
            * *ipAddress* (``str``)
            * *taskId* (``str``)
            * *sortyBy* (``str``)
            * *sortOrder* (``str``)
            * *ipAddress* (``str``)
            * *pingStatus* (``str``)
            * *snmpStatus* (``str``)
            * *cliStatus* (``str``)
            * *netconfStatus* (``str``)
            * *httpStatus* (``str``)
        :return:
        """
        allowed_kwargs = ['taskId', 'sortyBy', 'sortOrder', 'ipAddress', 'pingStatus', 'snmpStatus', 'cliStatus', 'netconfStatus', 'httpStatus']
        url = '/discovery/{}/summary'.format(discovery_id)
        url_params = handle_kwargs(params={}, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=url_params if url_params else None))

    def discovery_jobs_for_ip(self, ip, **kwargs):
        """

        :param ip:
        :param kwargs: See Keyword Arguments below
        :return:
        """
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
        return self.response_handler(self.get_handler(url))


class NetworkDiscovery(GlobalCredentials, Discoveries):
    """API to the Network Discovery section of the Cisco DNA Center REST API
    Version 1.1. Info on raw API calls can be found at https://developer.cisco.com/site/dna-center-rest-api/?version=1.1"""
    pass