from unittest import TestCase
from dnac_api.RequestHandler import ResponseObject
from tests.test_request_handler.testable_objects import TestableRequestHandler as RequestHandler


class TestGet(TestCase):

    def setUp(self) -> None:
        t = RequestHandler()
        self.data = t.get('url')

    def test_returns_response_object(self):
        self.assertEqual(ResponseObject, type(self.data))

    def test_extracts_response_properly(self):
        self.assertEqual({'results': 'junk'}, self.data.response_data)

    def test_extracts_status_code_properly(self):
        self.assertEqual(200, self.data.status_code)


class TestPost(TestGet):

    def setUp(self) -> None:
        t = RequestHandler()
        self.data = t.post('url', 'data')


class TestPut(TestGet):

    def setUp(self) -> None:
        t = RequestHandler()
        self.data = t.put('url', 'data')


class TestDelete(TestGet):

    def setUp(self) -> None:
        t = RequestHandler()
        self.data = t.delete('url')