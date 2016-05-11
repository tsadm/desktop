from unittest import TestCase
from tsdesktop import service

class TestService(TestCase):
    srvcs = None

    def setUp(self):
        if self.srvcs is None:
            self.srvcs = [c() for _, c in service._srvMap.items()]

    def test_service_class_map_name(self):
        for name in service._srvMap.keys():
            s = service.new(name)
            self.assertEqual(s.name, name)

    def test_service_detach(self):
        for s in self.srvcs:
            if s.name == 'httpd':
                self.assertFalse(s.detach)
            else:
                self.assertTrue(s.detach)

    def test_service_preChecks(self):
        for s in self.srvcs:
            if s.name == 'httpd':
                self.assertFalse(s.preChecks())
            else:
                self.assertTrue(s.preChecks())

    def test_service_runArgs(self):
        from os import path
        for s in self.srvcs:
            s.preChecks()
            if s.name == 'mysqld':
                self.assertEqual(s._datadir,
                    path.expanduser('~/.cache/tsdesktop/service/mysqld/datadir'))
                self.assertListEqual(s.runArgs,
                    ['-v', s._datadir+':/var/lib/mysql'])
            elif s.name == 'httpd':
                self.assertEqual(s.site.docroot,
                    path.join(path.abspath(path.curdir), 'docroot'))
                self.assertListEqual(s.runArgs,
                    ['-p', '127.0.0.1:33380:80',
                     '-v', s.site.docroot+':/var/www/html'])
            else:
                self.assertListEqual(s.runArgs, [])
