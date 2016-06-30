from unittest import TestCase
from tsdesktop import config
from sys import stdout
from os.path import expanduser

class Config(TestCase):

    def setUp(self):
        mock()

    def test_defaults(self):
        mock({'user': {}, 'site:fake2': {}})
        self.assertEqual(config.cfg.get('user', 'cachedir'),
            expanduser('~/.local/tsdesktop'))
        self.assertEqual(config.cfg.get('site:fake2', 'docroot'), 'docroot')

    def test_write(self):
        config.write()

# mock config for testing

def mock(cfg=None):
    config.filepath = '/dev/null'
    config.cfg = None
    config._init()
    config.cfg.read_dict({
        'site:fake.test': {'docroot': '/tmp'},
    })
    if cfg is not None:
        config.cfg.read_dict(cfg)

def dump():
    config.cfg.write(stdout)
