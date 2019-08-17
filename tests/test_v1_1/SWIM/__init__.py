from tests.controlled_objects import ControlledDNAServer
from dnac_api.v1_1.SWIM import SWIM


class TestableSWIM(SWIM, ControlledDNAServer):

    def __init__(self):
        ControlledDNAServer.__init__(self)
        SWIM.__init__(self)