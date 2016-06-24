from tsdesktop import config
from tsdesktop.testing import TSDesktopTest
from .siteman import siteRemove, siteAdd, siteOpen
from bottle import HTTPResponse

class Views(TSDesktopTest):

    def setUp(self):
        config._mock()

    def test_siteRemove404(self):
        r = siteRemove('fake.none')
        self.assertResponsePlain(r, code=404)

    def test_siteRemove(self):
        r = siteRemove('fake.test')
        self.assertResponsePlain(r)

    def test_siteOpen(self):
        with self.assertRaises(HTTPResponse) as cm:
            siteOpen('fake.test2', '/var/tmp')
        self.assertRedirect(cm.exception, location='/siteman/fake.test2/view')

    def test_siteOpenInvalid(self):
        r = siteOpen('fake/test', '/var/tmp')
        self.assertResponseError(r, code=400)

    def test_siteOpenExists(self):
        r = siteOpen('fake.test', '/var/tmp')
        self.assertResponseError(r, code=400)
