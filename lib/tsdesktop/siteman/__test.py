from tsdesktop.testing import TSDesktopTest
from tsdesktop import siteman, config_test

class Site(TSDesktopTest):

    def test_Site(self):
        s = siteman.Site('fake.test', '/var/www/html')
        self.assertEqual(s.name, 'fake.test')
        self.assertEqual(s.docroot, '/var/www/html')
        self.assertEqual(str(s), '<Site: fake.test>')

    def test_SiteNoDocroot(self):
        s = siteman.Site('fake.test', '/nonexistent')
        err = s.load()
        self.assertEqual(err, 'path not found')

    def test_SiteNotDir(self):
        s = siteman.Site('fake.test', '/usr/bin/env')
        err = s.load()
        self.assertEqual(err, 'not a dir')

    def test_siteAddError(self):
        err = siteman.siteAdd('fake.test', '/nonexistent')
        self.assertEqual(err, 'path not found')

    def test_siteGetNoDocroot(self):
        config_test.mock({'site:fake.test2': {'fake': 'test'}})
        s = siteman.siteGet('fake.test2')
        self.assertIsNone(s)
