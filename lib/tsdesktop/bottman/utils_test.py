from tsdesktop.testing import TSDesktopTest
from .utils import staticFile
from .views import dashboard
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
        if not self.skipOSX():
            v = dashboard.view()
            self.assertLinesContains(v, '<!DOCTYPE html>')
            self.assertLinesContains(v, '<html>')
            self.assertLinesContains(v, '<head>')
            self.assertLinesContains(v, '</head>')
            self.assertLinesContains(v, '<body class=')
            self.assertLinesContains(v, '</body>')
            self.assertLinesContains(v, '</html>')
