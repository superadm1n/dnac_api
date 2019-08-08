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

class SWIMAPI(DNAServer):

    # TODO: Add Post and Delete routes to API.

    def files_on_device(self, device_id):
        url = '/device-image/device/{}/file'.format(device_id)
        return self.response_handler(self.get_handler(url))

    def file_systems_on_device(self, device_id):
        url = '/device-image/device/{}/file-system'.format(device_id)
        return self.response_handler(self.get_handler(url))

    def image_details_with_filter(self, **kwargs):
        '''
        Reference API documentation for list of keyword arguments available
        https://developer.cisco.com/site/dna-center-rest-api/?version=1.1
        '''
        url = '/image/importation'
        return self.response_handler(self.get_handler(url, params=kwargs))

    def num_images_in_swim(self, **kwargs):
        '''
        Reference API documentation for list of keyword arguments available
        https://developer.cisco.com/site/dna-center-rest-api/?version=1.1
        '''
        url = '/image/importation/count'
        return self.response_handler(self.get_handler(url, params=kwargs))

    def image_by_uuid(self, image_uuid):
        url = '/image/importation/{}'.format(image_uuid)
        return self.response_handler(self.get_handler(url))

    def patch_details_respect_to_base_image(self, image_uuid, site_uuid, device_type_ordinal):
        url = '/image/importation/{image_uuid}/site/{site_uuid}/deviceType/{device_type_ordinal}/patch'.format(
            **{'image_uuid': image_uuid, 'site_uuid': site_uuid, 'device_type_ordinal': device_type_ordinal})
        return self.response_handler(self.get_handler(url))

    def recommended_image(self, device_uuid):
        url = '/image/recommendation/device/{}'.format(device_uuid)
        return self.response_handler(self.get_handler(url))
