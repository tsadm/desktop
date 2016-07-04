from tsdesktop.dockman import services

def _newService(name):
    k = services.classMap.get(name, None)
    if k is None:
        return None
    return k()

def start(service):
    print('start service: %s' % service)
    s = _newService(service)
    if s is None:
        print('invalid service: %s' % service)
        return 1
    err = s.start()
    if err is not None:
        print('service error: %s' % err)
        return 2
    return 0

def stop(service):
    print('stop service: %s' % service)
    s = _newService(service)
    if s is None:
        print('invalid service: %s' % service)
        return 1
    err = s.stop()
    if err is not None:
        print('service error: %s' % err)
        return 2
    return 0
