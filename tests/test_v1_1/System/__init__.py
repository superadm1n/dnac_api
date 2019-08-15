from tests.controlled_objects import ControlledDNAServer
from dnac_api.v1_1.System import System


class TestableSystem(System, ControlledDNAServer):
    def __init__(self):
        ControlledDNAServer.__init__(self)
        System.__init__(self)