from tsdesktop.testing import TSDesktopTest
from tsdesktop import siteman

class Site(TSDesktopTest):

    def test_Site(self):
        s = siteman.Site('fake.test', '/var/www/html')
        self.assertEqual(s.name, 'fake.test')
        self.assertEqual(s.docroot, '/var/www/html')
        self.assertEqual(str(s), '<Site: fake.test>')
