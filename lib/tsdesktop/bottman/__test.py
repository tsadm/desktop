from tsdesktop import config_test
from tsdesktop.testing import TSDesktopTest
from . import static, error400, error404, error405, error500, settings, about
import bottle

class Views(TSDesktopTest):

    def test_static(self):
        v = static('w3.css')
        self.assertIsInstance(v, bottle.HTTPResponse)

    def test_error400(self):
        v = error400(bottle.HTTPError(400, 'fake error'))
        self.assertLinesContains(v, '<h3>ERROR - 400')

    def test_error404(self):
        v = error404(bottle.HTTPError(404, 'fake error'))
        self.assertLinesContains(v, '<h3>ERROR - 404')

    def test_error405(self):
        v = error405(bottle.HTTPError(405, 'fake error'))
        self.assertLinesContains(v, '<h3>ERROR - 405')

    def test_error500(self):
        v = error500(bottle.HTTPError(500, 'fake error'))
        self.assertLinesContains(v, '<h3>ERROR - 500')

    def test_settings(self):
        config_test.mock()
        v = settings()
        self.assertLinesContains(v, '[DEFAULT]')
        self.assertLinesContains(v, 'docroot = docroot')

    def test_about(self):
        v = about()
        self.assertLinesContains(v, '<h3>tsdesktop v')
