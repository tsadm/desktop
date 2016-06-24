from unittest import TestCase
from tsdesktop import config

class Config(TestCase):

    def setUp(self):
        config.filepath = '/dev/null'
        config.read()


    def test_defaults(self):
        from os.path import expanduser
        fpathPrev = config.filepath
        config.cfg = None
        config.read()
        with self.assertRaises(KeyError):
            config.cfg['tsadm']

        self.assertEqual(config.cfg.get('user', 'cachedir'),
            expanduser('~/.cache/tsdesktop'))

        self.assertEqual(config.cfg.get('site', 'docroot'), 'docroot')


    def test_write(self):
        config.write()


    def test_httpd(self):
        httpd = config.cfg['service:httpd']
        self.assertTrue(httpd.getboolean('enable'))


    def test_mysqld(self):
        mysqld = config.cfg['service:mysqld']
        self.assertTrue(mysqld.getboolean('enable'))


# -- mock config for testing

def mock(cfg):
    config.filepath = '/dev/null'
    config.cfg = None
    config._init()
    config.cfg.read_dict(cfg)
