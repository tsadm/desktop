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
    queue = None

    def __init__(self):
        self.queue = tuple()

    def mock(self, *args):
        self.queue += tuple(args)

    def _qget(self, default=None):
        try:
            r = self.queue[0]
        except IndexError:
            return default
        self.queue = self.queue[1:]
        return r

    def ping(self):
        if self.pingFail:
            raise Exception('fake ping exception')

    def containers(self, **kwargs):
        return self._qget(default=[{}])

    def images(self, **kwargs):
        return self._qget(default=[{}])

    def version(self):
        return {}

    def pull(self, **kwargs):
        return self._qget(default='')

    def create_container(self, **kwargs):
        return {}

    def remove_container(self, **kwargs):
        pass

    def start(self, **kwargs):
        return self._qget()

    def stop(self, *args, **kwargs):
        return self._qget()

    def create_host_config(self, *args, **kwargs):
        pass

def _mockClient():
    global _cli
    _cli = _mock()
    return _cli
