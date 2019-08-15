from tests.controlled_objects import ControlledDNAServer
from dnac_api.v1_1.NetworkHost import NetworkHost


class TestableNetworkHost(NetworkHost, ControlledDNAServer):
    def __init__(self):
        ControlledDNAServer.__init__(self)
        NetworkHost.__init__(self)