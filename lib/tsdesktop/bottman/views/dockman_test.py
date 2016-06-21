from tsdesktop.testing import TSDesktopTest
from .dockman import dockman
from bottle import HTTPResponse

class Views(TSDesktopTest):

    def test_dockman(self):
        v = dockman()
        self.assertLinesContains(v,
            '<div id="dockman_mysqld" class="w3-modal">')

    def test_pullImage(self):
        with self.assertRaises(HTTPResponse) as cm:
            dockman('mysqld', 'pull-image')
        resp = cm.exception
        self.assertEqual(resp.status_code, 302)
        loc = resp.get_header('Location')
        self.assertEqual(loc, 'http://127.0.0.1/dockman')
