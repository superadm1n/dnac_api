from unittest import TestCase
from dnac_api.RequestHandler import ResponseObject
from tests.test_request_handler.testable_objects import TestableRequestHandler as RequestHandler
from http import HTTPStatus


class TestGet(TestCase):
    """
    Tests the get method and also serves as the base test to propegate each test
    to the other methods below
    """

    def setUp(self) -> None:
        t = RequestHandler()
        self.data = t.get('url')

    def test_returns_response_object(self):
        self.assertEqual(ResponseObject, type(self.data))

    def test_extracts_response_properly(self):
        self.assertEqual({'results': 'junk'}, self.data.response_data)

    def test_extracts_status_code_properly(self):
        self.assertEqual(200, self.data.status_code)
        self.assertEqual(HTTPStatus.OK, self.data.status_code)


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