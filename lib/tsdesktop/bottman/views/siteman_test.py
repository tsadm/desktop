from tsdesktop import config, config_test
from tsdesktop.testing import TSDesktopTest
from .siteman import rmSite, siteAdd, siteOpen
from bottle import HTTPResponse

class Views(TSDesktopTest):

    def setUp(self):
        config_test.mock()

    def test_siteRemove404(self):
        r = rmSite('fake.none')
        self.assertResponsePlain(r, code=404)
        self.assertEqual(r.body, 'site not found: fake.none')

    def test_siteRemove(self):
        r = rmSite('fake.test')
        self.assertResponsePlain(r)
        self.assertEqual(r.body, 'site removed: fake.test')

    def test_siteOpen(self):
        with self.assertRaises(HTTPResponse) as cm:
            siteOpen('fake1.test', '/var/tmp')
        self.assertRedirect(cm.exception, location='/siteman/fake1.test/view')

    def test_siteOpenInvalid(self):
        r = siteOpen('fake/test', '/var/tmp')
        self.assertResponseError(r, code=400)
        self.assertEqual(r.body, 'invalid site name: fake/test')

    def test_siteOpenExists(self):
        r = siteOpen('fake.test', '/var/tmp')
        self.assertResponseError(r, code=400)
        self.assertEqual(r.body, 'site already exists: fake.test')

    def test_siteOpenDupDocroot(self):
        r = siteOpen('fake.test3', '/var/www/site.fake/docroot')
        self.assertResponseError(r, code=400)
        self.assertEqual(r.body, 'could not load site: path not found')
