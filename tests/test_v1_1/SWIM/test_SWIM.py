from tests.test_v1_1.SWIM import TestableSWIM
from unittest import TestCase

class files_on_device(TestCase):

    def test_passes_proper_url(self):
        instance = TestableSWIM()
        device_id = '50'
        url = '/device-image/device/{}/file'.format(device_id)
        id = instance.files_on_device(device_id)
        self.assertEqual(url, instance.get_handler_passed_url[id])


class file_systems_on_device(TestCase):

    def test_passes_proper_url(self):
        instance = TestableSWIM()
        device_id = 50
        url = '/device-image/device/{}/file-system'.format(device_id)
        id = instance.file_systems_on_device(device_id)
        self.assertEqual(url, instance.get_handler_passed_url[id])

class image_details_with_filter(TestCase):

    def test_passes_proper_url(self):
        instance = TestableSWIM()
        url = '/image/importation'
        id = instance.image_details_with_filter()
        self.assertEqual(url, instance.get_handler_passed_url[id])

class num_images_in_swim(TestCase):

    def test_passes_proper_url(self):
        instance = TestableSWIM()
        url = '/image/importation/count'
        id = instance.num_images_in_swim()
        self.assertEqual(url, instance.get_handler_passed_url[id])

class image_by_uuid(TestCase):

    def test_passes_proper_url(self):
        instance = TestableSWIM()
        uuid = 50
        url = '/image/importation/{}'.format(uuid)
        id = instance.image_by_uuid(uuid)
        self.assertEqual(url, instance.get_handler_passed_url[id])


class patch_details_respect_to_base_image(TestCase):
    def test_passes_proper_url(self):
        instance = TestableSWIM()
        image_uuid = 'img'
        site_uuid = 'siteid'
        device_type_ordinal = 'ordinal'
        url = '/image/importation/{image_uuid}/site/{site_uuid}/deviceType/{device_type_ordinal}/patch'.format(
                **{'image_uuid': image_uuid, 'site_uuid': site_uuid, 'device_type_ordinal': device_type_ordinal})
        id = instance.patch_details_respect_to_base_image(image_uuid, site_uuid, device_type_ordinal)
        self.assertEqual(url, instance.get_handler_passed_url[id])

class recommended_image(TestCase):

    def test_passes_proper_url(self):
        instance = TestableSWIM()
        uuid = 50
        url = '/image/recommendation/device/{}'.format(uuid)
        id = instance.recommended_image(uuid)
        self.assertEqual(url, instance.get_handler_passed_url[id])