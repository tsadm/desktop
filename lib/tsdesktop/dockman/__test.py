from tsdesktop.testing import TSDesktopTest
from tsdesktop import dockman
import docker

class Client(TSDesktopTest):

    def test_getClient(self):
        dockman._cli = None
        cli = dockman.getClient()
        self.assertIsInstance(cli, docker.Client)

    def test_outputDecodeError(self):
        r = dockman.checkOutput('{}{}')
        self.assertIsNone(r)

    def test_outputError(self):
        r = dockman.checkOutput('{"error": "fake error message"}')
        self.assertIsNotNone(r)
        self.assertEqual(r, 'fake error message')
