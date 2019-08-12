from tests.test_v1_1.NetworkDiscovery.testable_objects import TestableGlobalCredentials as GlobalCredentials
from unittest import TestCase


class credential_sub_type(TestCase):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.id_used = 'junk'
        self.execution_id = self.instance.credential_sub_type(self.id_used)

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential/junk')

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)


class cli(TestCase):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global_credential'
        self.execution_id = self.instance.cli()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential')

    def test_accepts_proper_kwargs(self):
        acceptable_kwargs = {'sortBy': 'junk', 'order': 'junk'}
        id = self.instance.cli(**acceptable_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'credentialSubType': 'CLI', 'order': 'junk', 'sortBy': 'junk'})

    def test_exception_on_bad_kwarg(self):
        bad_kwargs = {'bad_kwarg': 'junk', 'order': 'junk'}
        with self.assertRaises(KeyError):
            self.instance.cli(**bad_kwargs)

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_always_passes_credentialSubType(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], {'credentialSubType': 'CLI'})


class create_cli_credentials(TestCase):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global-credential/cli'
        self.execution_id = self.instance.create_cli_credentials('username', 'password', 'enable_password', 'comments', 'description')
        self.expected_body_payload = [{'username': 'username', 'password': 'password', 'enablePassword': 'enable_password', 'comments': 'comments', 'description': 'description'}]

    def test_passes_proper_url(self):
        self.assertEqual(self.expected_url, self.instance.post_handler_passed_url[self.execution_id])

    def test_passes_proper_body_payload(self):
        self.assertEqual(self.expected_body_payload, self.instance.post_handler_passed_data[self.execution_id])


class snmpv2_read(TestCase):
    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global_credential'
        self.execution_id = self.instance.snmpv2_read()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential')

    def test_accepts_proper_kwargs(self):
        acceptable_kwargs = {'sortBy': 'junk', 'order': 'junk'}
        id = self.instance.snmpv2_read(**acceptable_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'credentialSubType': 'SNMPV2_READ_COMMUNITY', 'order': 'junk', 'sortBy': 'junk'})

    def test_exception_on_bad_kwarg(self):
        bad_kwargs = {'bad_kwarg': 'junk', 'order': 'junk'}
        with self.assertRaises(KeyError):
            self.instance.snmpv2_read(**bad_kwargs)

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_always_passes_credentialSubType(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], {'credentialSubType': 'SNMPV2_READ_COMMUNITY'})


class create_snmpv2_read(create_cli_credentials):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global-credential/snmpv2-read-community'
        self.execution_id = self.instance.create_snmpv2_read('string', 'comment', 'description')
        self.expected_body_payload = [{"readCommunity": 'string', "comments": 'comment', "description": 'description'}]


class snmpv2_write(TestCase):
    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global_credential'
        self.execution_id = self.instance.snmpv2_write()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential')

    def test_accepts_proper_kwargs(self):
        acceptable_kwargs = {'sortBy': 'junk', 'order': 'junk'}
        id = self.instance.snmpv2_write(**acceptable_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'credentialSubType': 'SNMPV2_WRITE_COMMUNITY', 'order': 'junk', 'sortBy': 'junk'})

    def test_exception_on_bad_kwarg(self):
        bad_kwargs = {'bad_kwarg': 'junk', 'order': 'junk'}
        with self.assertRaises(KeyError):
            self.instance.snmpv2_write(**bad_kwargs)

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_always_passes_credentialSubType(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], {'credentialSubType': 'SNMPV2_WRITE_COMMUNITY'})


class create_snmpv2_write(create_cli_credentials):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global-credential/snmpv2-write-community'
        self.execution_id = self.instance.create_snmpv2_write('string', 'comment', 'description')
        self.expected_body_payload = [{"writeCommunity": 'string', "comments": 'comment', "description": 'description'}]

class snmpv3(TestCase):
    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global_credential'
        self.execution_id = self.instance.snmpv3()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential')

    def test_accepts_proper_kwargs(self):
        acceptable_kwargs = {'sortBy': 'junk', 'order': 'junk'}
        id = self.instance.snmpv3(**acceptable_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'credentialSubType': 'SNMPV3', 'order': 'junk', 'sortBy': 'junk'})

    def test_exception_on_bad_kwarg(self):
        bad_kwargs = {'bad_kwarg': 'junk', 'order': 'junk'}
        with self.assertRaises(KeyError):
            self.instance.snmpv3(**bad_kwargs)

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_always_passes_credentialSubType(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], {'credentialSubType': 'SNMPV3'})


class create_snmpv3_credentials(create_cli_credentials):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global-credential/snmpv3'
        self.execution_id = self.instance.create_snmpv3_credentials(**{"privacy_password": 'privacy_password', "privacy_type": 'privacy_type', "snmp_mode": 'snmp_mode',
                                       "auth_type": 'auth_type', "auth_password": 'auth_password', "username": 'username', "comments": 'comments',
                                       "description": 'description'})
        self.expected_body_payload = [{"privacyPassword": 'privacy_password', "privacyType": 'privacy_type', "snmpMode": 'snmp_mode',
                                       "authType": 'auth_type', "authPassword": 'auth_password', "username": 'username', "comments": 'comments',
                                       "description": 'description'}]

class http_write(TestCase):
    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global_credential'
        self.execution_id = self.instance.http_write()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential')

    def test_accepts_proper_kwargs(self):
        acceptable_kwargs = {'sortBy': 'junk', 'order': 'junk'}
        id = self.instance.http_write(**acceptable_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'credentialSubType': 'HTTP_WRITE', 'order': 'junk', 'sortBy': 'junk'})

    def test_exception_on_bad_kwarg(self):
        bad_kwargs = {'bad_kwarg': 'junk', 'order': 'junk'}
        with self.assertRaises(KeyError):
            self.instance.http_write(**bad_kwargs)

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_always_passes_credentialSubType(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], {'credentialSubType': 'HTTP_WRITE'})


class create_http_write_credentials(create_cli_credentials):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global-credential/http-write'
        self.execution_id = self.instance.create_http_write_credentials('uname', 'pw', 50, True, 'comment', 'descrip')
        self.expected_body_payload = [{"port": 50, "secure": True, "username": 'uname', "password": 'pw', "comments": 'comment',
                                       "description": 'descrip'} ]

class http_read(TestCase):
    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global_credential'
        self.execution_id = self.instance.http_read()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential')

    def test_accepts_proper_kwargs(self):
        acceptable_kwargs = {'sortBy': 'junk', 'order': 'junk'}
        id = self.instance.http_read(**acceptable_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'credentialSubType': 'HTTP_READ', 'order': 'junk', 'sortBy': 'junk'})

    def test_exception_on_bad_kwarg(self):
        bad_kwargs = {'bad_kwarg': 'junk', 'order': 'junk'}
        with self.assertRaises(KeyError):
            self.instance.http_read(**bad_kwargs)

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_always_passes_credentialSubType(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], {'credentialSubType': 'HTTP_READ'})


class create_http_read_credentials(create_cli_credentials):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global-credential/http-read'
        self.execution_id = self.instance.create_http_read_credentials('uname', 'pw', 50, True, 'comment', 'descrip')
        self.expected_body_payload = [{"port": 50, "secure": True, "username": 'uname', "password": 'pw', "comments": 'comment',
                                       "description": 'descrip'} ]

class netconf(TestCase):
    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global_credential'
        self.execution_id = self.instance.netconf()

    def test_passes_proper_url(self):
        self.assertEqual(self.instance.get_handler_passed_url[self.execution_id], '/global-credential')

    def test_accepts_proper_kwargs(self):
        acceptable_kwargs = {'sortBy': 'junk', 'order': 'junk'}
        id = self.instance.netconf(**acceptable_kwargs)
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[id], {'credentialSubType': 'NETCONF', 'order': 'junk', 'sortBy': 'junk'})

    def test_exception_on_bad_kwarg(self):
        bad_kwargs = {'bad_kwarg': 'junk', 'order': 'junk'}
        with self.assertRaises(KeyError):
            self.instance.netconf(**bad_kwargs)

    def test_calls_response_handler(self):
        self.assertEqual(self.instance.response_handler_called, 1)

    def test_always_passes_credentialSubType(self):
        self.assertEqual(self.instance.get_handler_passed_url_paramenters[self.execution_id], {'credentialSubType': 'NETCONF'})

class create_netconf_credentials(create_cli_credentials):

    def setUp(self) -> None:
        self.instance = GlobalCredentials()
        self.expected_url = '/global-credential/netconf'
        self.execution_id = self.instance.create_netconf_credentials('50', 'comment', 'descrip')
        self.expected_body_payload = [{"netconfPort": '50', "comments": 'comment', "description": 'descrip'}]