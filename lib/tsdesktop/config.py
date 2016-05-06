from os.path import expanduser
from configparser import ConfigParser

cfg = None

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

def read(filenames=None):
    _init()
    if filenames is None:
        filenames = [expanduser("~/.tsdesktop.ini"), ".tsdesktop.ini"]
    return cfg.read(filenames)
