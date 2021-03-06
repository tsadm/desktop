from tsdesktop.testing import TSDesktopTest
from tsdesktop import dockman
import docker

class Client(TSDesktopTest):

    def test_getClient(self):
        if not self.skipOSX():
            dockman._cli = None
            cli = dockman.getClient()
            self.assertIsInstance(cli, docker.Client)

    def test_outputDecodeError(self):
        r = dockman._checkOutput('{}{}')
        self.assertIsNone(r)

    def test_outputError(self):
        r = dockman._checkOutput('{"error": "fake error message"}')
        self.assertIsNotNone(r)
        self.assertEqual(r, 'fake error message')
