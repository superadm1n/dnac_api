from tests.test_v1_1.NetworkDiscovery.testable_objects import TestableDiscoveries as Discoveries
from unittest import TestCase



class number_of_discoveries(TestCase):

    def setUp(self) -> None:
        self.instance = Discoveries()
        self.execution_id = self.instance.number_of_discoveries

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/discovery/count')


class discovery_by_id(TestCase):
    def setUp(self) -> None:
        self.passed_id = 'junk'
        self.instance = Discoveries()
        self.execution_id = self.instance.discovery_by_id(self.passed_id)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/discovery/{}'.format(self.passed_id))


class discovery_jobs_by_id(TestCase):
    def setUp(self) -> None:
        self.passed_id = 'junk'
        self.instance = Discoveries()
        self.execution_id = self.instance.discovery_jobs_by_id(self.passed_id)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/discovery/{}/job'.format(self.passed_id))

    def test_accepts_kwargs(self):
        kwargs = {'offset': 'junk', 'limit': 'junk', 'ipAddress': 'junk'}
        id = self.instance.discovery_jobs_by_id(self.passed_id, **kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'offset': 'junk', 'limit': 'junk', 'ipAddress': 'junk'})

    def test_fails_with_bad_kwarg(self):
        kwargs = {'offset': 'junk', 'limit': 'junk', 'ipAddress': 'junk', 'badkwarg': 'badkwarg'}
        with self.assertRaises(KeyError):
            self.instance.discovery_jobs_by_id(self.passed_id, **kwargs)


class network_devices_from_discovery_by_filters(TestCase):

    def setUp(self) -> None:
        self.passed_id = 'junk'
        self.instance = Discoveries()
        self.execution_id = self.instance.network_devices_from_discovery_by_filters(self.passed_id)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/discovery/{}/summary'.format(self.passed_id))

    def test_accepts_kwargs(self):
        kwargs = {'taskId': 'junk', 'sortyBy': 'junk', 'sortOrder': 'junk', 'ipAddress': 'junk', 'pingStatus': 'junk', 'snmpStatus': 'junk',
                  'cliStatus': 'junk', 'netconfStatus': 'junk', 'httpStatus': 'junk'}
        id = self.instance.network_devices_from_discovery_by_filters(self.passed_id, **kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], kwargs)

    def test_fails_with_bad_kwarg(self):
        kwargs = {'offset': 'junk', 'limit': 'junk', 'ipAddress': 'junk', 'badkwarg': 'badkwarg'}
        with self.assertRaises(KeyError):
            self.instance.discovery_jobs_by_id(self.passed_id, **kwargs)


class discovery_jobs_for_ip(TestCase):

    def setUp(self) -> None:
        self.passed_id = 'junk'
        self.instance = Discoveries()
        self.execution_id = self.instance.discovery_jobs_for_ip(self.passed_id)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/discovery/job')

    def test_accepts_kwargs(self):
        kwargs = {'offset': 'junk', 'limit': 'junk', 'name': 'junk'}
        id = self.instance.discovery_jobs_for_ip(self.passed_id, **kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'ipAddress': 'junk', 'limit': 'junk', 'name': 'junk', 'offset': 'junk'})

    def test_fails_with_bad_kwarg(self):
        kwargs = {'offset': 'junk', 'limit': 'junk', 'ipAddress': 'junk', 'badkwarg': 'badkwarg'}
        with self.assertRaises(KeyError):
            self.instance.discovery_jobs_by_id(self.passed_id, **kwargs)


class num_network_devices_in_discovery(TestCase):
    def setUp(self) -> None:
        self.passed_id = 'junk'
        self.instance = Discoveries()
        self.execution_id = self.instance.num_network_devices_in_discovery(self.passed_id)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/discovery/{}/network-device/count'.format(self.passed_id))


class physical_topology(TestCase):
    def setUp(self) -> None:
        self.instance = Discoveries()
        self.execution_id = self.instance.physical_topology()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/topology/physical-topology')
