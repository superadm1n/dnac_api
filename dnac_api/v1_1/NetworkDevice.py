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
        """gets the number of network devices by sending a get request to ``/network-device/count``

        :return: number of network devices
        """
        url = '/network-device/count'
        return self.response_handler(self.get_handler(url))

    def network_devices(self, id=None):
        """Returns the network devices

        :param id: Filters devices returned that match ID
        :return:
        """
        url = '/network-device'
        return self.response_handler(self.get_handler(url, params={'id': id} if id else None))

    def network_device_by_ip(self, ip):
        """Sends get request to ``/network-device/ip-address/{ip}``

        :param ip: IP address to search by
        :return: Network device associated with IP
        """
        url = '/network-device/ip-address/{}'.format(ip)
        return self.response_handler(self.get_handler(url))

    def network_device_by_serial_number(self, device_serial_number):
        """Gets network device by serial number by sending a get request to ``/network-device/serial-number/{sn}``

        :param device_serial_number:
        :return:
        """
        url = '/network-device/serial-number/{}'.format(device_serial_number)
        return self.response_handler(self.get_handler(url))

    def network_device_by_id(self, id):
        """Gets network device by ID by sending a get request to ``/network-device/{id}``

        :param id: ID to search by
        :return: Network device
        """
        url = '/network-device/{}'.format(id)
        return self.response_handler(self.get_handler(url))

    def network_device_brief_by_id(self, id):
        """Similar to ``network_device_by_id(id)`` but returns brief data.

        :param id: ID to search by
        :return: Network device data - brief
        """
        url = '/network-device/{}/brief'.format(id)
        return self.response_handler(self.get_handler(url))


class Modules(DNAServer):

    def modules_in_device(self, device_id, **kwargs):
        """Returns the modules in device. Sends a get request to ``/network-device/module``

        :param device_id: ID of network device
        :param kwargs: See Keyword Arguments below
        :Keyword Arguments:
            * *limit* (``str``)
            * *offset* (``str``)
            * *nameList* (``str``)
            * *vendorEquipmentTypeList* (``str``)
            * *partNumberList* (``str``)
            * *operationalStateCodeList* (``str``)
            * *deviceId* (``str``)
        :return:
        """
        allowed_kwargs = ['limit', 'offset', 'nameList', 'vendorEquipmentTypeList', 'partNumberList', 'operationalStateCodeList', 'deviceId']
        url = '/network-device/module'
        params = {'deviceId': device_id}
        params = handle_kwargs(params, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=params))

    def number_of_modules_in_device(self, device_id, **kwargs):
        """Returns the number of modules in a device. Sends get request to ``/network-device/module/count``

        :param device_id: Device ID of network device
        :param kwargs: See Keyword Arguments below
        :Keyword Arguments:
            * *deviceId* (``str``)
            * *nameList* (``str``)
            * *vendorEquipmentTypeList* (``str``)
            * *partNumberList* (``str``)
            * *operationalStateCodeList* (``str``)

        :return:
        """
        allowed_kwargs = ['deviceId', 'nameList', 'vendorEquipmentTypeList', 'partNumberList', 'operationalStateCodeList']
        url = '/network-device/module/count'
        params = {'deviceId': device_id}
        params = handle_kwargs(params, allowed_kwargs=allowed_kwargs, **kwargs)
        return self.response_handler(self.get_handler(url, params=params))

    def module_info_by_id(self, module_id):
        """Gets info related to module by the ID of the module. Sends get request to ``/network-device/module/{module_id}``

        :param module_id: ID of module to return data about
        :return: Module info
        """
        url = '/network-device/module/{}'.format(module_id)
        return self.response_handler(self.get_handler(url))


class Locations(DNAServer):

    @property
    def devices_with_location(self):
        """Get location data about devices. Sends get request to ``/network-device/location``

        :return:
        """
        url = '/network-device/location'
        return self.response_handler(self.get_handler(url))

    def devices_at_location(self, location_id):
        """Get devices at location by location ID. Sends get request to ``/network-device/location/{location_id}``

        :param location_id: ID of location to search by
        :return: List of devices
        """
        url = '/network-device/location/{}'.format(location_id)
        return self.response_handler(self.get_handler(url))

    def location_by_device_id(self, device_id):
        """Returns the location of a device when specifying the device ID. Sends get request to ``/network-device/{device_id}/location``

        :param device_id: ID of network device
        :return: Location information
        """
        url = '/network-device/{}/location'.format(device_id)
        return self.response_handler(self.get_handler(url))


class NetworkDevice(DeviceOperations, Locations, Modules):
    pass
