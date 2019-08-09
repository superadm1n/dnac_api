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


class DeviceOperations(DNAServer):

    @property
    def network_device_count(self):
        url = '/network-device/count'
        return self.response_handler(self.get_handler(url))

    def network_devices(self, id=None):
        url = '/network-device'
        return self.response_handler(self.get_handler(url, params={'id': id} if id else None))

    def network_device_by_ip(self, ip):
        url = '/network-device/ip-address/{}'.format(ip)
        return self.response_handler(self.get_handler(url))

    def network_device_by_serial_number(self, device_serial_number):
        url = '/network-device/serial-number/{}'.format(device_serial_number)
        return self.response_handler(self.get_handler(url))

    def network_device_by_id(self, id):
        url = '/network-device/{}'.format(id)
        return self.response_handler(self.get_handler(url))

    def network_device_brief_by_id(self, id):
        url = '/network-device/{}/brief'.format(id)
        return self.response_handler(self.get_handler(url))


class Modules(DNAServer):

    def modules_in_device(self, device_id, **kwargs):
        allowed_kwargs = ['limit', 'offset', 'nameList', 'vendorEquipmentTypeList', 'partNumberList', 'operationalStateCodeList', 'deviceId']
        url = '/network-device/module'
        params = {'deviceId': device_id}
        params = handle_kwargs(params, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=params))

    def number_of_modules_in_device(self, device_id, **kwargs):
        allowed_kwargs = ['deviceId', 'nameList', 'vendorEquipmentTypeList', 'partNumberList', 'operationalStateCodeList']
        url = '/network-device/module/count'
        params = {'deviceId': device_id}
        params = handle_kwargs(params, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=params))

    def module_info_by_id(self, module_id):
        url = '/network-device/module/{}'.format(module_id)
        return self.response_handler(self.get_handler(url))


class Locations(DNAServer):

    @property
    def devices_with_location(self):
        '''My DOcumentation

        :return:
        '''
        url = '/network-device/location'
        return self.response_handler(self.get_handler(url))

    def devices_at_location(self, location_id):
        url = '/network-device/location/{}'.format(location_id)
        return self.response_handler(self.get_handler(url))

    def location_by_device_id(self, device_id):
        url = '/network-device/{}/location'.format(device_id)
        return self.response_handler(self.get_handler(url))


class NetworkDevice(DeviceOperations, Locations, Modules):
    pass
