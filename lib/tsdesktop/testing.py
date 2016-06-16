import platform
from unittest import TestCase

class TSDesktopTest(TestCase):

    def skipOSX(self):
        print(platform.system())
        if platform.system() == 'Darwin':
            self.skipTest('tsdesktop skipOSK')
            return True
        return False

    def assertLinesContains(self, src, text):
        lno = 0
        found = 0
        for l in src.splitlines():
            lno += 1
            try:
                l.index(text)
            except ValueError:
                pass
            else:
                found = lno
                break
        self.assertTrue(found, msg='not found: '+text)
