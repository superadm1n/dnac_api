from unittest import TestCase
from tests.test_v1_1.NetworkHost.testable_objects import TestableNetworkHost as NetworkHost

class num_of_hosts(TestCase):

    def setUp(self) -> None:
        self.instance = NetworkHost()
        self.func = self.instance.num_of_hosts
        self.good_kwargs = {'hostName': 'junk', 'hostMac': 'junk', 'hostType': 'junk', 'connectedInterfaceName': 'junk', 'hostIp': 'junk',
                       'connectedNetworkDeviceIpAddress': 'junk', 'connectedNetworkDeviceName': 'junk', 'hostDeviceType': 'junk', 'subType': 'junk'}
        self.bad_kwargs = {'bad_kwarg': 'badkwarg'}
        self.expected_url = '/host/count'

    def test_allowed_kwargs(self):
        id = self.func(**self.good_kwargs)
        self.assertEqual(self.good_kwargs, self.instance.get_handler_passed_url_paramenters[id])

    def test_bad_kwargs(self):
        with self.assertRaises(KeyError):
            self.func(**self.bad_kwargs)

    def test_passes_proper_url(self):
        id = self.func()
        self.assertEqual(self.expected_url, self.instance.get_handler_passed_url[id])


class hosts_by_filter(num_of_hosts):

    def setUp(self) -> None:
        self.instance = NetworkHost()
        self.func = self.instance.hosts_by_filter
        self.good_kwargs = {'limit': 'junk', 'offset': 'junk', 'sortBy': 'junk', 'order': 'junk', 'hostName': 'junk', 'hostMac': 'junk',
                       'hostType': 'junk', 'connectedInterfaceName': 'junk', 'hostIp': 'junk', 'connectedNetworkDeviceIpAddress': 'junk',
                       'connectedNetworkDeviceName': 'junk', 'hostDeviceType': 'junk', 'subType': 'junk'}
        self.bad_kwargs = {'bad_kwarg': 'badkwarg'}
        self.expected_url = '/host'


class host_by_id(TestCase):
    def setUp(self) -> None:
        self.instance = NetworkHost()

    def test_passes_proper_url(self):
        id = self.instance.host_by_id('50')
        self.assertEqual('/host/50', self.instance.get_handler_passed_url[id])
