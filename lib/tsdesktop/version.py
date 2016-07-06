import time
import json
from os import path
from getpass import getuser
from platform import node

VERSION = (16, 6, '3+next')
APPNAME = 'tsdesktop'

buildinfo = {
    'TIME': None,
}
binfoFile = path.join(path.dirname(__file__), 'buildinfo.json')

def writeBuildInfo():
    global buildinfo
    buildinfo['TIME'] = time.time()
    buildinfo['AUTHOR'] = getuser()
    buildinfo['HOSTNAME'] = node()
    with open(binfoFile, 'w') as fh:
        json.dump(buildinfo, fh)
        fh.close()

def readBuildInfo():
    global buildinfo
    try:
        with open(binfoFile, 'r') as fh:
            buildinfo = json.load(fh)
            fh.close()
    except IOError: # coverage: exclude
        pass

def _version():
    return '.'.join([str(i) for i in VERSION])

def string():
    readBuildInfo()
    v = "{} v{}".format(APPNAME, _version())
    if buildinfo['TIME'] is not None:
        v = "{} ({} {}@{})".format(
            v,
            time.strftime('%d%b%Y', time.localtime(buildinfo['TIME'])),
            buildinfo['AUTHOR'],
            buildinfo['HOSTNAME'],
        )
    return v

def println():
    print(string())

if __name__ == '__main__': # coverage: exclude
    println()
