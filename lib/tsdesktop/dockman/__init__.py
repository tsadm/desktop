import json
from docker import Client

_cli = None

def getClient():
    global _cli
    if _cli is None:
        _cli = Client(version='auto', timeout=15)
    return _cli

def checkOutput(out):
    for line in out.splitlines():
        try:
            l = json.loads(line)
            if 'error' in l.keys():
                return l.get('error')
        except ValueError:
            # XXX: ignoring json decode errors...
            pass
    return None

#
# -- mock client for testing
#

from queue import Queue, Empty

class _mock:

    queue = Queue()

    def mock(self, *args):
        for a in args:
            self.queue.put_nowait(a)

    def _qget(self):
        try:
            r = self.queue.get_nowait()
        except Empty:
            return None
        return r

    def ping(self):
        pass

    def containers(self, **kwargs):
        pass

    def images(self, **kwargs):
        pass

    def version(self):
        return {}

    def pull(self, **kwargs):
        r = self._qget()
        if r is not None:
            return r
        return ''

def _mockClient():
    global _cli
    _cli = _mock()
    return _cli
