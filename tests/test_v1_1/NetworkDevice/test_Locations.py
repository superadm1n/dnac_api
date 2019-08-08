from unittest import TestCase
from tests.test_v1_1.NetworkDevice.testable_objects import TestableLocations


class TestDevicesWithLocation(TestCase):

    def setUp(self) -> None:
        self.instance = TestableLocations()
        self.execution_id = self.instance.devices_with_location

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/location')

    def test_calls_response_handler_once(self):
        self.assertEqual(self.instance.response_handler_called, 1)


class TestDevicesAtLocation(TestCase):

    def setUp(self) -> None:
        self.id_used = 50
        self.instance = TestableLocations()
        self.execution_id = self.instance.devices_at_location(self.id_used)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/location/{}'.format(self.id_used))

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)


class TestLocationByDeviceId(TestCase):

    def setUp(self) -> None:
        self.id_used = 50
        self.instance = TestableLocations()
        self.execution_id = self.instance.location_by_device_id(self.id_used)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/{}/location'.format(self.id_used))