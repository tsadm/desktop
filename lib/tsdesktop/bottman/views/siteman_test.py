from tsdesktop import config
from tsdesktop.testing import TSDesktopTest
from .siteman import siteRemove, siteAdd, siteOpen
from bottle import HTTPResponse

class Views(TSDesktopTest):

    def setUp(self):
        config.filepath = '/dev/null'
        config.read()
        config.cfg.add_section('site:fake.test')
        config.cfg.set('site:fake.test', 'docroot', '/var/www/site.fake/docroot')

    def test_siteRemove404(self):
        r = siteRemove('fake.none')
        self.assertResponsePlain(r, code=404)

    def test_siteRemove(self):
        r = siteRemove('fake.test')
        self.assertResponsePlain(r, code=200)

    def test_siteOpen(self):
        with self.assertRaises(HTTPResponse) as cm:
            siteOpen('fake.test2', '/var/tmp')
        self.assertRedirect(cm.exception, location='http://127.0.0.1/siteman/fake.test2/view')
