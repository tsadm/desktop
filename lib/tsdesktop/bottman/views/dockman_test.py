from tsdesktop.testing import TSDesktopTest
from .dockman import view
from tsdesktop import dockman
from bottle import HTTPResponse, HTTPError

images = [{}]
containers = [{'Status': None}]

class Views(TSDesktopTest):
    cli = None

    def setUp(self):
        self.cli = dockman._mockClient()

    def test_dockman(self):
        r = view()
        self.assertLinesContains(r,
            '<div id="dockman_mysqld" class="w3-modal">')

    def test_dockmanActionInvalid(self):
        r = view('mysqld', 'invalid')
        self.assertResponse(r, 400)

    def test_dockmanPingFail(self):
        self.cli.pingFail = True
        with self.assertRaises(HTTPError) as cm:
            r = view()
        self.assertResponseError(cm.exception)

    def test_pullImage(self):
        with self.assertRaises(HTTPResponse) as cm:
            view('mysqld', 'pull-image')
        self.assertRedirect(cm.exception, location='/dockman')

    def test_pullImageInvalid(self):
        r = view('faked', 'pull-image')
        self.assertResponse(r, 400)

    def test_pullImageError(self):
        self.cli.mock(images, '{"error": "fake error"}')
        r = view('mysqld', 'pull-image')
        self.assertResponseError(r)

    def test_serviceStart(self):
        self.cli.mock([{'Status': ''}])
        with self.assertRaises(HTTPResponse) as cm:
            view('mysqld', 'start')
        self.assertRedirect(cm.exception, location='/dockman')

    def test_serviceStartError(self):
        self.cli.mock(containers)
        self.cli.mock('{"error": "service start fake error"}')
        r = view('mysqld', 'start')
        self.assertResponse(r, 400)

    def test_serviceStop(self):
        self.cli.mock([{
            'Status': 'Up since...',
            'Names': ['/tsdesktop-mysqld'],
        }])
        with self.assertRaises(HTTPResponse) as cm:
            r = view('mysqld', 'stop')
        self.assertRedirect(cm.exception, location='/dockman')

    def test_serviceStopError(self):
        self.cli.mock(containers)
        self.cli.mock('{"error": "service stop fake error"}')
        r = view('mysqld', 'stop')
        self.assertResponse(r, 400)
