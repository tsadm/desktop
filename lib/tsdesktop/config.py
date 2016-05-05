from sys import stdout
from os.path import expanduser
from configparser import ConfigParser

cfg = None

def _init():
    global cfg
    if cfg is None:
        cfg = ConfigParser()
        cfg['DEFAULT'] = {}

def read():
    _init()
    ok = cfg.read([expanduser("~/.tsdesktop.ini"), ".tsdesktop.ini"], 'utf8')
    print("read:", " ".join(ok), end="\n\n")
    cfg.write(stdout)
