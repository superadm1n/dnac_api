from dnac_api.RequestHandler import RequestHandler


class FakeRequestObject:
    """
    Designed to be a fake object returned from the requests library on a get, post
    delete, put request
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @property
    def status_code(self):
        return 200

    def json(self):
        return {'results': 'junk'}


class TestableRequestHandler(RequestHandler):

    def __init__(self):
        """
        Over ride init method to do nothing so we can specify our own
        variables to do the gets, posts, etc.
        """
        pass

    def _get(self, *args, **kwargs):
        return FakeRequestObject(*args, **kwargs)

    def _post(self, *args, **kwargs):
        return FakeRequestObject(*args, **kwargs)

    def _delete(self, *args, **kwargs):
        return FakeRequestObject(*args, **kwargs)

    def _put(self, *args, **kwargs):
        return FakeRequestObject(*args, **kwargs)

    def _request(self, *args, **kwargs):
        return FakeRequestObject(*args, **kwargs)