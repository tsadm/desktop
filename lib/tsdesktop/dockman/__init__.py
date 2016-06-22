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

class _mock:

    pingFail = False
    queue = tuple()

    def mock(self, *args):
        self.queue += tuple(args)

    def _qget(self):
        try:
            r = self.queue[0]
        except IndexError:
            return None
        self.queue = self.queue[1:]
        return r

    def ping(self):
        if self.pingFail:
            raise Exception('fake ping exception')

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

    def create_container(self, **kwargs):
        return dict()

    def start(self, **kwargs):
        pass

def _mockClient():
    global _cli
    _cli = _mock()
    return _cli
