from tsdesktop.testing import TSDesktopTest
from .utils import staticFile, textPlain
from . import about
import bottle


class StaticFile(TSDesktopTest):

    def test_staticFile(self):
        sf = staticFile('w3.css')
        self.assertIsInstance(sf, bottle.HTTPResponse)
        self.assertEqual(sf.status_code, 200)
        self.assertEqual(sf.charset, 'UTF-8')
        self.assertEqual(sf.content_length, 29467)
        self.assertEqual(sf.content_type, 'text/css; charset=UTF-8')

    def test_staticFileNotFound(self):
        sf = staticFile('w3.cssNOT_FOUND')
        self.assertEqual(sf.status_code, 404)


class Render(TSDesktopTest):

    def test_render(self):
        v = about()
        self.assertLinesContains(v, '<!DOCTYPE html>')
        self.assertLinesContains(v, '<html>')
        self.assertLinesContains(v, '<head>')
        self.assertLinesContains(v, '</head>')
        self.assertLinesContains(v, '<body class=')
        self.assertLinesContains(v, '</body>')
        self.assertLinesContains(v, '</html>')


class Plain(TSDesktopTest):

    def test_textPlain(self):
        r = textPlain('fake body')
        self.assertEqual(r.status_code, 200)
        ct = r.headers.get('Content-Type')
        self.assertEqual(ct, 'text/plain; charset=UTF-8')

    def test_textPlain400(self):
        r = textPlain('fake error 400', 400)
        self.assertEqual(r.status_code, 400)
        ct = r.headers.get('Content-Type')
        self.assertEqual(ct, 'text/plain; charset=UTF-8')
