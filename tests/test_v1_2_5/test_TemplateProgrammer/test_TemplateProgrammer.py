from unittest import TestCase
from tests.test_v1_2_5.test_TemplateProgrammer.testable_objects import TestableTemplateProgrammer
from dnac_api.RequestHandler import ResponseObject

class TestTemplatesAvailable(TestCase):

    def setUp(self) -> None:
        self.instance = TestableTemplateProgrammer()
        self.execution_id = self.instance.templates_available()

    def test_passes_url_properly(self):
        self.assertEqual('/template-programmer/template', self.instance.get_handler_passed_url[self.execution_id])


class TestProjects(TestCase):

    def setUp(self) -> None:
        self.instance = TestableTemplateProgrammer()
        self.execution_id = self.instance.projects()

    def test_passes_url_properly(self):
        self.assertEqual('/template-programmer/project', self.instance.get_handler_passed_url[self.execution_id])