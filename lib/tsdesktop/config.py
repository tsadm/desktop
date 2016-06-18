import sys
from os.path import expanduser
from configparser import ConfigParser

cfg = None
filepath = expanduser("~/.tsdesktop.ini")

def _init():
    global cfg
    if cfg is None:
        cfg = ConfigParser()
        cfg['DEFAULT'] = {}
        cfg['user'] = {
            'cachedir': expanduser('~/.cache/tsdesktop'),
        }
        cfg['service:httpd'] = {
            'enable': True,
        }
        cfg['service:mysqld'] = {
            'enable': True,
        }
        cfg['site'] = {
            'docroot': 'docroot',
        }

def write():
    _init()
    with open(filepath, 'w') as fh:
        cfg.write(fh)
        fh.close()

def read():
    _init()
    ok = cfg.read(filepath)
    if ok:
        return filepath
    else:
        return '(no config file)'

def cmd(): # coverage: exclude
    sys.stdout.write("read: "+filepath+"\n\n")
    cfg.write(sys.stdout)
    return 0
