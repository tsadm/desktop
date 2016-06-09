from docker import Client

_cli = None

def getClient():
    global _cli
    if _cli is None:
        _cli = Client(version='auto', timeout=15)
    return _cli
