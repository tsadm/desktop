from tsdesktop.testing import TSDesktopTest
from . import static, error400, error404, error500, settings, about
import bottle

class Views(TSDesktopTest):

    def test_static(self):
        v = static('w3.css')
        self.assertIsInstance(v, bottle.HTTPResponse)

    def test_error400(self):
        v = error400(bottle.HTTPError(400, 'fake error'))
        self.assertEqual(len(v), 1331)

    def test_error404(self):
        v = error404(bottle.HTTPError(404, 'fake error'))
        self.assertEqual(len(v), 1329)

    def test_error500(self):
        v = error500(bottle.HTTPError(500, 'fake error'))
        self.assertEqual(len(v), 1341)

    def test_settings(self):
        v = settings()
        self.assertEqual(len(v), 1267)

    def test_about(self):
        v = about()
        self.assertLinesContains(v, '<h3>tsdesktop v')
