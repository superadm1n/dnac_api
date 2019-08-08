from unittest import TestCase
from tests.test_v1_1.NetworkDevice.testable_objects import TestableModules


class TestModulesInDevice(TestCase):
    """
    tests the modules_in_device() method in the Modules class
    """

    def setUp(self) -> None:
        self.device_id_used = 50
        self.instance = TestableModules()
        self.execution_id = self.instance.modules_in_device(self.device_id_used)

    def test_passes_correct_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/module')

    def test_calls_response_handler_once(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_allows_correct_kwargs(self):
        kwargs = {'deviceId': 'junk', 'nameList': 'junk', 'vendorEquipmentTypeList': 'junk', 'partNumberList': 'junk', 'operationalStateCodeList': 'junk'}
        t = TestableModules()
        execution_id = t.modules_in_device(self.device_id_used, **kwargs)
        self.assertEqual(t.get_handler_passed_url_paramenters[execution_id], {'deviceId': 'junk', 'nameList': 'junk', 'vendorEquipmentTypeList': 'junk', 'partNumberList': 'junk', 'operationalStateCodeList': 'junk'})

    def test_exception_on_bad_kwargs(self):
        bad_kwargs = {'junk': 'junk'}
        t = TestableModules()
        with self.assertRaises(KeyError):
            t.modules_in_device(self.device_id_used, **bad_kwargs)


class TestNumberofModulesinDevice(TestCase):
    """
    Tests the "number_of_modules_in_device()" method in the Modules class
    """
    def setUp(self) -> None:
        self.device_id_used = 50
        self.instance = TestableModules()
        self.execution_id = self.instance.number_of_modules_in_device(self.device_id_used)

    def test_passes_correct_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/module/count')

    def test_calls_response_handler_once(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_allows_correct_kwargs(self):
        kwargs = {'deviceId': 'junk', 'nameList': 'junk', 'vendorEquipmentTypeList': 'junk', 'partNumberList': 'junk', 'operationalStateCodeList': 'junk'}
        t = TestableModules()
        execution_id = t.number_of_modules_in_device(self.device_id_used, **kwargs)
        self.assertEqual(t.get_handler_passed_url_paramenters[execution_id], {'deviceId': 'junk', 'nameList': 'junk', 'vendorEquipmentTypeList': 'junk', 'partNumberList': 'junk', 'operationalStateCodeList': 'junk'})

    def test_exception_on_bad_kwargs(self):
        bad_kwargs = {'junk': 'junk'}
        t = TestableModules()
        with self.assertRaises(KeyError):
            t.number_of_modules_in_device(self.device_id_used, **bad_kwargs)


class TestModuleInfoById(TestCase):
    """
    Tests the "module_info_by_id()" method in the Modules class
    """
    def setUp(self) -> None:
        self.module_id_used = 50
        self.instance = TestableModules()
        self.execution_id = self.instance.module_info_by_id(self.module_id_used)

    def test_passes_correct_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/network-device/module/{}'.format(self.module_id_used))

    def test_calls_response_handler_once(self):
        self.assertEqual(self.instance.response_handler_called, 1)
