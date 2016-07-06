import os
import time
import subprocess
from tsdesktop import siteman
from tsdesktop.dockman import services, pullImage

def _newService(name, site=None):
    if site is None:
        k = services.classMap.get(name, None)
        if k is None:
            print('invalid service: %s' % name)
            return None
        return k(site=site)
    else:
        s = siteman.siteGet(site)
        if s is None:
            print('invalid site: %s' % site)
            return None
        return s.webserver
    return None

def start(service, site=None):
    s = _newService(service, site)
    if s is None:
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

def login(service, site=None):
    s = _newService(service, site)
    if s is None:
        return 1
    stopService = False
    if s.status() != 'running':
        sts = start(service, site)
        if sts != 0:
            return sts
        stopService = True
    print('service login: %s' % s.containerName)
    cmd = ['docker', 'exec', '-it', s.containerName, '/bin/bash']
    p = subprocess.Popen(cmd)
    _, sts = os.waitpid(p.pid, 0)
    if sts != 0:
        return sts
    if stopService:
        return stop(service, site)
    return 0

def pull(service):
    s = _newService(service)
    if s is None:
        return 1
    img = s.imageInfo()
    err = pullImage(img.repo(), img.tag())
    if err is not None:
        print('pull error: %s' % err)
        return 2
    return 0

def importDB(dbserver, dbname):
    s = _newService(dbserver)
    if s is None:
        return 1
    print('%s database import: %s' % (dbserver, dbname))
    cmd = ['mysql', '-h', '127.0.0.1', '-P', '4936',
                                    '-u', 'tsdesktop', '-ptsdesktop', dbname]
    p = subprocess.Popen(cmd)
    _, sts = os.waitpid(p.pid, 0)
    return sts
