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


class NetworkHost(DNAServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = '/host'

    def hosts_by_filter(self, **kwargs):
        '''
        Parameter	        Description	                   Parameter_Type	DataType
        limit	            limit	                       query	        string
        offset    	        offset	                       query	        string
        sortBy    	        sortBy	                       query	        string
        order    	        order	                       query	        string
        hostName	        hostName	                   query	        List
        hostMac  	        hostMac  	                   query	        List
        hostType	        Host type : wired or wireless  query	        List
        connectedInterfaceName	connectedInterfaceName	   query	        List
        hostIp	            hostIp	                       query	        List
        connectedNetworkDeviceIpAddress	connectedNetworkDeviceIpAddress	query	List
        connectedNetworkDeviceName	connectedNetworkDeviceName	query	List
        hostDeviceType	hostDeviceType	query	List
        subType	Available values: 'UNKNOWN' or 'IP_PHONE' or 'TELEPRESENCE' or 'VIDEO_SURVEILLANCE_IP_CAMERA' or 'VIDEO_ENDPOINT'. Only exact match filtering supported on this field
        '''
        allowed_kwargs = ['limit', 'offset', 'sortBy', 'order', 'hostName', 'hostMac', 'hostType', 'connectedInterfaceName', 'hostIp',
                          'connectedNetworkDeviceIpAddress', 'connectedNetworkDeviceName', 'hostDeviceType', 'subType']
        params = handle_kwargs({}, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url='/host', params=params))

    @property
    def num_of_hosts(self, **kwargs):
        allowed_kwargs = ['hostName', 'hostMac', 'hostType', 'connectedInterfaceName', 'hostIp', 'connectedNetworkDeviceIpAddress',
                          'connectedNetworkDeviceName', 'hostDeviceType', 'subType']
        url = '/host/count'
        params = handle_kwargs({}, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=params))

    def host_by_id(self, id):
        url = '/host/{}'.format(id)
        return self.response_handler(self.get_handler(url))