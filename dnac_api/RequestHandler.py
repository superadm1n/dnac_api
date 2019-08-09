import requests


class ResponseObject:
    """
    This is the object that should be returned from any request
    """
    def __init__(self, status_code, response_data):
        self.status_code = status_code
        self.response_data = response_data


class RequestHandler:
    """
    This class is a wrapper for the requests api. It buys us the ability in the future to utilize a different
    package to handle the requests if it is decided. It also allows us to test the DNAServer class via
    dependency injection
    """
    def __init__(self):
        self._get = requests.get
        self._post = requests.post
        self._delete = requests.delete
        self._put = requests.put
        self._request = requests.request

    def _extract_data_from_raw(self, raw_data):
        """Not to be used outside this class, Takes the raw data, instantiates a request object
        and populates the relevant data from the raw data into the request object. Finally
        returning that instantiated object to the calling method.

        :param raw_data: Raw data as returned from the requests library
        :return: Request Object
        """
        return ResponseObject(status_code=raw_data.status_code, response_data=raw_data.json())

    def request(self, method, url, **kwargs):
        return self._extract_data_from_raw(self._request(method, url, **kwargs))

    def get(self, url, params=None, **kwargs):
        return self._extract_data_from_raw(self._get(url, params, **kwargs))

    def post(self, url, data, json=None, **kwargs):
        return self._extract_data_from_raw(self._post(url, data, json, **kwargs))

    def put(self, url, data, **kwargs):
        return self._extract_data_from_raw(self._put(url, data, **kwargs))

    def delete(self, url, **kwargs):
        return self._extract_data_from_raw(self._delete(url, **kwargs))
