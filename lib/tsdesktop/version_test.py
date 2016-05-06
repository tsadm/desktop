from unittest import TestCase
from tsdesktop import version

class TestVersion(TestCase):
    """mainly so version.py is not removed by mistake"""

    def test_version(self):
        self.assertIsInstance(version.VERSION, str)
