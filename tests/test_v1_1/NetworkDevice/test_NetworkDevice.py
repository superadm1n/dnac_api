from unittest import TestCase
from tests.test_v1_1.NetworkDevice.testable_objects import TestableNetworkDevice


class TestNetworkDeviceCount(TestCase):

    def setUp(self) -> None:
        self.instance = TestableNetworkDevice()
        self.execution_id = self.instance.network_device_count

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/count')


class TestNetworkDevice(TestCase):

    def setUp(self) -> None:
        self.instance = TestableNetworkDevice()
        self.execution_id = self.instance.network_devices()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device')

    def test_doesnt_pass_params_without_id_called(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], None)

    def test_handles_id_param(self):
        id = self.instance.network_devices('junk')
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id]['id'], 'junk')


class TestNetworkDeviceByIp(TestCase):

    def setUp(self) -> None:
        self.passed_value = 'junk'
        self.instance = TestableNetworkDevice()
        self.execution_id = self.instance.network_device_by_ip(self.passed_value)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/ip-address/{}'.format(self.passed_value))


class TestNetworkDeviceBySerialNumber(TestCase):

    def setUp(self) -> None:
        self.sn = 'junk'
        self.instance = TestableNetworkDevice()
        self.execution_id = self.instance.network_device_by_serial_number(self.sn)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/serial-number/{}'.format(self.sn))


class TestNetworkDeviceById(TestCase):

    def setUp(self) -> None:
        self.val = 'junk'
        self.instance = TestableNetworkDevice()
        self.execution_id = self.instance.network_device_by_id(self.val)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/{}'.format(self.val))


class TestNetworkDeviceBriefById(TestCase):

    def setUp(self) -> None:
        self.val = 'junk'
        self.instance = TestableNetworkDevice()
        self.execution_id = self.instance.network_device_brief_by_id(self.val)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/{}/brief'.format(self.val))
