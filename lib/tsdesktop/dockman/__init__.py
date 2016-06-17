import json
from docker import Client

_cli = None

def getClient():
    global _cli
    if _cli is None:
        _cli = Client(version='auto', timeout=15)
    return _cli

def checkOutput(out):
    print(type(out), out)
    lno = 0
    for line in out.splitlines():
        lno += 1
        try:
            l = json.loads(line)
            if 'error' in l.keys():
                return l.get('error')
        except json.decoder.JSONDecodeError as e:
            # XXX: ignoring json decode errors...
            pass
    return None
