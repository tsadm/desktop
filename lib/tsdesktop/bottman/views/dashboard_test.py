from tsdesktop import dockman
from tsdesktop.testing import TSDesktopTest
from .dashboard import view

class Views(TSDesktopTest):

    def setUp(self):
        dockman._mockClient()

    def test_dashboard(self):
        v = view()
        self.assertLinesContains(v,
            '<div id="dockman_mysqld" class="w3-modal">')
