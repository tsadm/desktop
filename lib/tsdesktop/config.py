import sys
from os.path import expanduser
from configparser import ConfigParser

cfg = None
filepath = expanduser("~/.tsdesktop.ini")

def _init():
    global cfg
    if cfg is None:
        cfg = ConfigParser()
        cfg['DEFAULT'] = {
            'docroot': 'docroot',
            'cachedir': expanduser('~/.cache/tsdesktop'),
        }

def write():
    _init()
    with open(filepath, 'w') as fh:
        cfg.write(fh)
        fh.close()
    # reload config
    _reload()

def _reload():
    global cfg
    cfg = None
    return read()

def read():
    _init()
    ok = cfg.read(filepath)
    if ok:
        return filepath
    else:
        return '(no config file)'

def cmd(): # coverage: exclude
    cfg.write(sys.stdout)
    return 0
