from tsdesktop import dockman, config_test
from tsdesktop.testing import TSDesktopTest
from .dashboard import view

class Views(TSDesktopTest):

    def setUp(self):
        config_test.mock()
        dockman._mockClient()

    def test_dashboard(self):
        v = view()
        self.assertLinesContains(v,
            '<div id="dockman_mysqld" class="w3-modal">')
