from tests.test_v1_1.controlled_dna_server import ControlledDNAServer
from dnac_api.v1_1.NetworkDiscovery import GlobalCredentials, Discoveries


class TestableGlobalCredentials(GlobalCredentials, ControlledDNAServer):
    """
    Injects the ControlledDNAServer ahead of the DNAServer in the MRO of the GlobalCredentials class so we can test the GlobalCredentials
    object
    """
    def __init__(self):
        ControlledDNAServer.__init__(self)
        GlobalCredentials.__init__(self)


class TestableDiscoveries(Discoveries, ControlledDNAServer):
    """
    Injects the ControlledDNAServer ahead of the DNAServer in the MRO of the Discoveries class so we can test the Discoveries
    object
    """
    def __init__(self):
        ControlledDNAServer.__init__(self)
        Discoveries.__init__(self)