from tsdesktop.testing import TSDesktopTest
from .dockman import dockman

class Views(TSDesktopTest):

    def test_dockman(self):
        v = dockman()
        self.assertLinesContains(v,
            '<div id="dockman_mysqld" class="w3-modal">')
