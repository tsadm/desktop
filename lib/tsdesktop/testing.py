from unittest import TestCase

class TSDesktopTest(TestCase):

    def assertLinesContains(self, src, text):
        lno = 0
        found = 0
        for l in src.splitlines():
            lno += 1
            if l.find(text) > 0:
                found = lno
                break
        self.assertTrue(found, msg='not found: '+text)
