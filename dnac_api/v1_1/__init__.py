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


This file imports each of the sections of the v1.1 Cisco DNA Center
API so each object is presented to the user with its proper name.
"""
from dnac_api.v1_1.NetworkDevice import NetworkDevice
from dnac_api.v1_1.NetworkDiscovery import NetworkDiscovery
from dnac_api.v1_1.NetworkHost import NetworkHost
from dnac_api.v1_1.SWIM import SWIM
from dnac_api.v1_1.System import System
