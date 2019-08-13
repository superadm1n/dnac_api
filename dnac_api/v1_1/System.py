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

class System(DNAServer):

    # TODO: Add the Put, Post, and Delete routes to the API

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def available_namespaces(self):
        """Lists available namespaces. Sends get request to ``/file/namespace``

        :return:
        """
        url = '/file/namespace'
        return self.response_handler(self.get_handler(url))

    def files_under_namespace(self, namespace):
        """Gets files located under namespace. sends get request to ``/file/namespace/{namespace}``

        :param namespace:
        :return: Files
        """
        url = '/file/namespace/{}'.format(namespace)
        return self.response_handler(self.get_handler(url))

    def file_checksum_by_field(self, field):
        """Gets file checksum by field. Sends a get request to ``/file/{field}/checksum``

        :param field:
        :return: File checksum
        """
        url = '/file/{}/checksum'.format(field)
        return self.response_handler(self.get_handler(url))
