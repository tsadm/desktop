from unittest import TestCase
from bottle import HTTPResponse

class TSDesktopTest(TestCase):

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

    def assertResponse(self, resp, code=200):
        self.assertIsInstance(resp, HTTPResponse)
        self.assertEqual(resp.status_code, code)
