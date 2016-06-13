from unittest import TestCase
from tsdesktop import version

class TestVersion(TestCase):
    """mainly so version.py is not removed by mistake"""
    def test_version(self):
        self.assertIsInstance(version.APPNAME, str)
        self.assertIsInstance(version.VERSION, tuple)
        self.assertIsInstance(version.string(), str)
