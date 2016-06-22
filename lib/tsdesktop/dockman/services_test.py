from tsdesktop.testing import TSDesktopTest
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
