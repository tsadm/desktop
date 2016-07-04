import os
import subprocess
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
