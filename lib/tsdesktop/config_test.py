from unittest import TestCase
from tsdesktop import config

class TestConfig(TestCase):
    def setUp(self):
        config.read('/dev/null')

    def test_service_defaults(self):
        with self.assertRaises(KeyError):
            config.cfg['tsadm']

    def test_service_httpd(self):
        httpd = config.cfg['service:httpd']
        self.assertTrue(httpd.getboolean('enable'))

    def test_service_mysqld(self):
        mysqld = config.cfg['service:mysqld']
        self.assertTrue(mysqld.getboolean('enable'))
