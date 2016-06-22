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

    def ping(self):
        pass

    def containers(self, **kwargs):
        pass

    def images(self, **kwargs):
        pass

    def version(self):
        return {}

    def pull(self, **kwargs):
        return ''

def _mockClient():
    global _cli
    _cli = _mock()
    return _cli
