import platform
from unittest import TestCase
from bottle import HTTPResponse, HTTPError

class TSDesktopTest(TestCase):

    def skipOSX(self):
        if platform.system().lower() == 'darwin':
            self.skipTest('skip test under mac osx')
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

    def assertResponse(self, resp, code=200, klass=HTTPResponse):
        self.assertIsInstance(resp, klass)
        self.assertEqual(resp.status_code, code)

    def assertResponseError(self, resp, code=500):
        self.assertResponse(resp, code=code, klass=HTTPError)

    def assertResponsePlain(self, resp, code=200):
        self.assertResponse(resp, code=code)
        ct = resp.get_header('Content-Type')
        self.assertEqual(ct, 'text/plain; charset=UTF-8')

    def assertRedirect(self, resp, location='/', code=302):
        self.assertIsInstance(resp, HTTPResponse)
        self.assertEqual(resp.status_code, code)
        loc = resp.get_header('Location')
        loc = loc.replace('http://127.0.0.1', '')
        self.assertEqual(loc, location)
