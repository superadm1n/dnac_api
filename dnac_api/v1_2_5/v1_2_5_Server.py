from dnac_api.Server import DNAServer as BaseDNAServer


class DNAServer(BaseDNAServer):
    """
    This class handles interfacing the api level of the package with the handling of the requests to the DNA server.
    It provides a standard way for the rest of the package to send data to the DNA Center server.
    """

    def __new__(cls, *args, **kwargs):
        cls = super().__new__(cls)
        cls.base_url_string = 'https://{}/dna/intent/api/v1'
        cls.login_url_string = 'https://{}/api/system/v1/auth/token'
        return cls
