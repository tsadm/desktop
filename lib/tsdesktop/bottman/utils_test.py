from unittest import TestCase
from .utils import staticFile
from .views import dashboard
import bottle


class StaticFile(TestCase):

    def test_staticFile(self):
        sf = staticFile('w3.css')
        self.assertIsInstance(sf, bottle.HTTPResponse)
        self.assertEqual(sf.status_code, 200)
        self.assertEqual(sf.charset, 'UTF-8')
        self.assertEqual(sf.content_length, 29467)
        self.assertEqual(sf.content_type, 'text/css; charset=UTF-8')

    def test_staticFileNotFound(self):
        sf = staticFile('w3.cssNOT_FOUND')
        self.assertEqual(sf.status_code, 404)


class Render(TestCase):

    def test_render(self):
        v = dashboard.view()
        self.assertEqual(len(v), 2378)
