import sys
from os.path import expanduser
from configparser import ConfigParser

cfg = None
readFiles = []

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

def read(filenames=None):
    global readFiles
    _init()
    if filenames is None:
        filenames = [expanduser("~/.tsdesktop.ini"), ".tsdesktop.ini"]
    ok = cfg.read(filenames)
    readFiles = ok or ['(no config files)']
    return readFiles

def cmd(): # coverage: exclude
    ok = read()
    sys.stdout.write("read: "+" ".join(ok)+"\n\n")
    cfg.write(sys.stdout)
    return 0
