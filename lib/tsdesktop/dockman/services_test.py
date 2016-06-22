from tsdesktop.testing import TSDesktopTest
from tsdesktop import dockman
from tsdesktop.dockman import services

class ImageInfo(TSDesktopTest):

    def test_statusError(self):
        i = services.ImageInfo('faked', error=True)
        self.assertEqual(i.status, 'error')

    def test_statusMissing(self):
        i = services.ImageInfo('faked', missing=True)
        self.assertEqual(i.status, 'missing')

    def test_statusOK(self):
        i = services.ImageInfo('faked', info=True)
        self.assertEqual(i.status, 'ok')

    def test_tag(self):
        i = services.ImageInfo('tsadm/desktop:faked', info=True)
        self.assertEqual(i.tag(), 'faked')

    def test_tagError(self):
        i = services.ImageInfo('faked', info=True)
        self.assertEqual(i.tag(), '')

images = [{'RepoTags': ['tsadm/desktop:faked']}]
containers = [{'Status': None}]

class Service(TSDesktopTest):

    def setUp(self):
        self.cli = dockman._mockClient()
        self.srvc = services.Service()
        self.srvc.name = 'faked'

    def test_imageInfo(self):
        self.cli.mock(images)
        i = self.srvc.imageInfo()
        self.assertEqual(i.status, 'ok')

    def test_imageInfoMissing(self):
        self.cli.mock([{}])
        i = self.srvc.imageInfo()
        self.assertEqual(i.status, 'missing')

    def test_imageInfoError(self):
        self.cli.mock([])
        i = self.srvc.imageInfo()
        self.assertEqual(i.status, 'error')

    def test_statusEmpty(self):
        self.cli.mock([])
        s = self.srvc.status()
        self.assertEqual(s, '')

    def test_statusNone(self):
        self.cli.mock(containers)
        s = self.srvc.status()
        self.assertEqual(s, 'error')

    def test_statusRunning(self):
        self.cli.mock([{'Status': 'Up since...'}])
        s = self.srvc.status()
        self.assertEqual(s, 'running')

    def test_statusExit(self):
        self.cli.mock([{'Status': 'Exited at...'}])
        s = self.srvc.status()
        self.assertEqual(s, 'exit')

    def test_statusError(self):
        self.cli.mock([{'Status': ''}])
        s = self.srvc.status()
        self.assertEqual(s, 'error')
