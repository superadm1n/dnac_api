from tests.controlled_objects import ControlledDNAServer
from dnac_api.v1_2_5.TemplateProgrammer import TemplateProgrammer


class TestableTemplateProgrammer(TemplateProgrammer, ControlledDNAServer):
    '''
    Injects controlled dna server so we can test the TemplateProgrammer class.
    '''
    def __init__(self):
        ControlledDNAServer.__init__(self)
