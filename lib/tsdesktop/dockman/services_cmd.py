import os
import time
import subprocess
from tsdesktop.dockman import services

def _newService(name, site=None):
    k = services.classMap.get(name, None)
    if k is None:
        return None
    return k(site=site)

def start(service, site=None):
    s = _newService(service, site)
    if s is None:
        print('invalid service: %s' % service)
        return 1
    print('start service: %s' % s.containerName)
    err = s.start()
    if err is not None:
        print('service error: %s' % err)
        return 2
    print(s.URI)
    if s.URIDesc:
        print(s.URIDesc)
    return 0

def stop(service, site=None):
    s = _newService(service, site)
    if s is None:
        print('invalid service: %s' % service)
        return 1
    print('stop service: %s' % s.containerName)
    err = s.stop()
    if err is not None:
        print('service error: %s' % err)
        return 2
    return 0

def restart(service, site=None):
    stop(service, site)
    time.sleep(1)
    return start(service, site)

def importDB(dbserver, dbname):
    print('%s database import: %s' % (dbserver, dbname))
    s = _newService(dbserver)
    if s is None:
        print('invalid database server: %s' % dbserver)
        return 1
    cmd = ['mysql', '-h', '127.0.0.1', '-P', '4936',
                                    '-u', 'tsdesktop', '-ptsdesktop', dbname]
    print('cmd:', ' '.join(cmd))
    p = subprocess.Popen(cmd)
    _, sts = os.waitpid(p.pid, 0)
    return sts
