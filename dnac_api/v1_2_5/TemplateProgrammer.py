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
from dnac_api.v1_2_5.v1_2_5_Server import DNAServer


class TemplateProgrammer(DNAServer):

    def templates_available(self):
        '''Lists the templates available. Submits get request to /template-programmer/template

        :return: Templates available
        :rtype: list
        '''
        return self.get_handler('/template-programmer/template')

    def projects(self):
        return self.get_handler('/template-programmer/project')