from unittest import TestCase
from tsdesktop import version

class TestVersion(TestCase):

    def test_version(self):
        self.assertIsInstance(version.APPNAME, str)
        self.assertIsInstance(version.VERSION, tuple)
        self.assertIsInstance(version.string(), str)

    def test_buildinfo(self):
        version.writeBuildInfo()
