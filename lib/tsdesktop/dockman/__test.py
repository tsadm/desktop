from tsdesktop.testing import TSDesktopTest
from tsdesktop import dockman
import docker

class Client(TSDesktopTest):

    def test_getClient(self):
        dockman._cli = None
        cli = dockman.getClient()
        self.assertIsInstance(cli, docker.Client)
