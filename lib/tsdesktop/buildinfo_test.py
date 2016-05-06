from unittest import TestCase
from tsdesktop import buildinfo

class TestBuildinfo(TestCase):
    """mainly so buildinfo.py is not removed by mistake"""

    def test_buildinfo(self):
        self.assertIsNone(buildinfo.ID)
        self.assertIsNone(buildinfo.DATE)
        self.assertIsNone(buildinfo.AUTHOR)
