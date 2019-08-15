from unittest import TestCase
from tests.controlled_objects import ControlledDNAServer
from dnac_api.v1_1.NetworkHost import NetworkHost


class TestableNetworkHost(NetworkHost, ControlledDNAServer):

    def __init__(self):
        ControlledDNAServer.__init__(self)
        NetworkHost.__init__(self)


class hosts_by_filter(TestCase):
    def setUp(self) -> None:
        self.instance = TestableNetworkHost()
        self.execution_id = self.instance.hosts_by_filter()

    def test_sends_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/host')

    def test_accepts_proper_kwargs(self):
        allowed_kwargs = {'limit': 'junk', 'offset': 'junk', 'sortBy': 'junk', 'order': 'junk', 'hostName': 'junk', 'hostMac': 'junk',
                          'hostType': 'junk', 'connectedInterfaceName': 'junk', 'hostIp': 'junk', 'connectedNetworkDeviceIpAddress': 'junk',
                          'connectedNetworkDeviceName': 'junk', 'hostDeviceType': 'junk', 'subType': 'junk'}
        id = self.instance.hosts_by_filter(**allowed_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], allowed_kwargs)
        pass

    def test_exception_on_incorrect_kwargs(self):
        bad_kwargs = {'badkwarg': 'badkwarg'}
        with self.assertRaises(KeyError):
            self.instance.hosts_by_filter(**bad_kwargs)
