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
    return cfg.read([expanduser("~/.tsdesktop.ini"), ".tsdesktop.ini"], 'utf8')
