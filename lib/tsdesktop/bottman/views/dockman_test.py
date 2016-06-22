from tsdesktop.testing import TSDesktopTest
from .dockman import view
from tsdesktop import dockman
from bottle import HTTPResponse, HTTPError

class Views(TSDesktopTest):
    cli = None

    def setUp(self):
        self.cli = dockman._mockClient()

    def test_dockman(self):
        r = view()
        self.assertLinesContains(r,
            '<div id="dockman_mysqld" class="w3-modal">')

    def test_pullImage(self):
        with self.assertRaises(HTTPResponse) as cm:
            view('mysqld', 'pull-image')
        r = cm.exception
        self.assertEqual(r.status_code, 302)
        loc = r.get_header('Location')
        self.assertEqual(loc, 'http://127.0.0.1/dockman')

    def test_pullImageInvalid(self):
        r = view('faked', 'pull-image')
        self.assertIsInstance(r, HTTPError)
        self.assertEqual(r.status_code, 400)

    def test_pullImageError(self):
        self.cli.mock('{"error": "fake error"}')
        r = view('mysqld', 'pull-image')
        self.assertIsInstance(r, HTTPError)
        self.assertEqual(r.status_code, 500)
