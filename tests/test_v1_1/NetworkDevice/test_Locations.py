from unittest import TestCase
from tests.test_v1_1.NetworkDevice.testable_objects import TestableLocations


class TestDevicesWithLocation(TestCase):

    def setUp(self) -> None:
        self.instance = TestableLocations()
        self.execution_id = self.instance.devices_with_location

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/location')


class TestDevicesAtLocation(TestCase):

    def setUp(self) -> None:
        self.id_used = 50
        self.instance = TestableLocations()
        self.execution_id = self.instance.devices_at_location(self.id_used)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/location/{}'.format(self.id_used))


class TestLocationByDeviceId(TestCase):

    def setUp(self) -> None:
        self.id_used = 50
        self.instance = TestableLocations()
        self.execution_id = self.instance.location_by_device_id(self.id_used)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/{}/location'.format(self.id_used))