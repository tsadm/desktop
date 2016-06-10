from unittest import TestCase
from . import static, error400, error404, error500, settings
import bottle

class Views(TestCase):

    def test_static(self):
        v = static('w3.css')
        self.assertIsInstance(v, bottle.HTTPResponse)

    def test_error400(self):
        v = error400(bottle.HTTPError(400, 'fake error'))
        self.assertEqual(len(v), 1310)

    def test_error404(self):
        v = error404(bottle.HTTPError(404, 'fake error'))
        self.assertEqual(len(v), 1308)

    def test_error500(self):
        v = error500(bottle.HTTPError(500, 'fake error'))
        self.assertEqual(len(v), 1320)

    def test_settings(self):
        v = settings()
        self.assertEqual(len(v), 1246)
