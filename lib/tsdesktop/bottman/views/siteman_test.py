from tsdesktop import config
from tsdesktop.testing import TSDesktopTest
from .siteman import siteRemove

class Views(TSDesktopTest):

    @classmethod
    def setUpClass(self):
        config.cfg.add_section('site:fake.test')
        config.cfg.set('site:fake.test', 'docroot', '/var/www/site.fake/docroot')

    def test_siteRemove404(self):
        r = siteRemove('fake.none')
        self.assertResponsePlain(r, code=404)

    def test_siteRemove(self):
        r = siteRemove('fake.test')
        self.assertResponsePlain(r, code=200)
