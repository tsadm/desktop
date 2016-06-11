import time
import json
from os import path

VERSION = '16.6'
APPNAME = 'tsdesktop'

buildinfo = {
    'TIME': None,
}
binfoFile = path.join(path.dirname(__file__), 'buildinfo.json')

def writeBuildInfo():
    global buildinfo
    buildinfo['TIME'] = time.time()
    with open(binfoFile, 'w') as fh:
        json.dump(buildinfo, fh)
        fh.close()

def readBuildInfo():
    global buildinfo
    try:
        with open(binfoFile, 'r') as fh:
            buildinfo = json.load(fh)
            fh.close()
    except IOError:
        pass

def println():
    readBuildInfo()
    v = "{} v{}".format(APPNAME, VERSION)
    if buildinfo['TIME'] is not None:
        v = "{} ({})".format(v, buildinfo['TIME'])
    print(v)

if __name__ == '__main__': # coverage: exclude
    println()
