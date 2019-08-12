from tests.test_v1_1.System import TestableSystem
from unittest import TestCase


class available_namespaces(TestCase):

    def test_passes_url_properly(self):
        instance = TestableSystem()
        url = '/file/namespace'
        id = instance.available_namespaces
        self.assertEqual(url, instance.get_handler_passed_url[id])


class files_under_namespace(TestCase):

    def test_passes_url_properly(self):
        namespace = 'mynamespace'
        url = '/file/namespace/{}'.format(namespace)
        instance = TestableSystem()
        id = instance.files_under_namespace(namespace)
        self.assertEqual(url, instance.get_handler_passed_url[id])

class file_checksum_by_field(TestCase):

    def test_passes_url_properly(self):
        field = 'field'
        url = '/file/{}/checksum'.format(field)
        instance = TestableSystem()
        id = instance.file_checksum_by_field(field)
        self.assertEqual(url, instance.get_handler_passed_url[id])