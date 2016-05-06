from unittest import TestCase
from tsdesktop import service

class TestService(TestCase):
    srvcs = None

    def setUp(self):
        if self.srvcs is None:
            self.srvcs = [c() for _, c in service.srvMap.items()]

    def test_service_class_map_name(self):
        for name in service.srvMap.keys():
            s = service.srvMap.get(name)()
            self.assertEqual(s.name, name)

    def test_service_detach(self):
        for s in self.srvcs:
            if s.name == 'httpd':
                self.assertFalse(s.detach)
            else:
                self.assertTrue(s.detach)

    def test_service_preChecks(self):
        for s in self.srvcs:
            s.preChecks()

    def test_service_runArgs(self):
        from os.path import expanduser
        for s in self.srvcs:
            if s.name == 'mysqld':
                self.assertEqual(s._datadir,
                    expanduser('~/.cache/tsdesktop/service/mysqld/datadir'))
                self.assertListEqual(s.runArgs,
                    ['-v', s._datadir+':/var/lib/mysql'])
            else:
                self.assertListEqual(s.runArgs, [])
