from tsdesktop.testing import TSDesktopTest
from tsdesktop import siteman, config_test

class Site(TSDesktopTest):

    def setUp(self):
        config_test.mock()

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

    #~ def test_siteAddError(self):
        #~ err = siteman.siteAdd('fake.test2', '/nonexistent')
        #~ self.assertEqual(err, 'path not found')

    def test_siteGetNoDocroot(self):
        config_test.mock({'site:fake.test2': {}})
        s = siteman.siteGet('fake.test2')
        self.assertEqual(s.docroot, 'docroot')

    def test_sitesAll(self):
        c = {
            'site:fake2.test': {'docroot': '/tmp'},
            'site:fake3.test': {'docroot': '/tmp'},
        }
        config_test.mock(c)
        l = sorted([str(i) for i in siteman.sitesAll()])
        self.assertListEqual(l, sorted([
            str(siteman.Site('fake.test', '/ignored')),
            str(siteman.Site('fake2.test', '/ignored')),
            str(siteman.Site('fake3.test', '/ignored')),
        ]))

    def test_sitesAllInvalidName(self):
        c = {'site:test;invalid': {'docroot': '/ignored'}}
        config_test.mock(c)
        l = siteman.sitesAll()
        self.assertIsNone(l)
