from dnac_api.v1_1.NetworkDevice import Locations, Modules, NetworkDevice
from tests.test_v1_1.controlled_dna_server import ControlledDNAServer


class TestableLocations(Locations, ControlledDNAServer):
    """
    Injects the ControlledDNAServer ahead of the DNAServer in the MRO of the Locations class so we can test the Locations
    object
    """

    def __init__(self):
        ControlledDNAServer.__init__(self)


class TestableModules(Modules, ControlledDNAServer):
    """
    Injects the ControlledDNAServer ahead of the DNAServer in the MRO of the Modules class so we can test the Modules
    object
    """
    def __init__(self):
        ControlledDNAServer.__init__(self)


class TestableNetworkDevice(NetworkDevice, ControlledDNAServer):
    """
    Injects the ControlledDNAServer ahead of the DNAServer in the MRO of the NetworkDevice class so we can test the NetworkDevice
    object
    """
    def __init__(self):
        ControlledDNAServer.__init__(self)

