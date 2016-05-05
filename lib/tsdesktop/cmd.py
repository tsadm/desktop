import sys

def _serviceCmd(name, action):
    from tsdesktop.service import cmdMap
    kls = cmdMap.get(name, None)
    if kls is None:
        print("E: invalid service:", name)
        return 2
    srv = kls()
    return srv.action(action)

def main():
    if sys.argv[1] == "service":
        return _serviceCmd(sys.argv[2], sys.argv[3])
    else:
        print("E: invalid command:", sys.argv[1])
        return 1
    return 0
