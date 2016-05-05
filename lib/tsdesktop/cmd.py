import sys

def _serviceCmd(name, action):
    from tsdesktop.service import cmdMap
    kls = cmdMap.get(name, None)
    if kls is None:
        print("E: invalid command")
        return 1
    srv = kls()
    return srv.action(action)

def main():
    if sys.argv[1] == "service":
        return _serviceCmd(sys.argv[2], sys.argv[3])
    return 0
