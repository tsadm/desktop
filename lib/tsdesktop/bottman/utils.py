from os import path
import bottle
from bottle import template, static_file, request
from tsdesktop import version
from time import strftime

_tplsDir = path.abspath(path.join(path.dirname(__file__), 'templates'))
_staticDir = path.join(_tplsDir, 'static')
bottle.TEMPLATE_PATH.insert(0, _tplsDir)


def render(tpl, **kwargs):
    tdata = {
        'appName': version.APPNAME,
        'appVersion': version.VERSION,
        'req': request,
        'now': strftime('%a %b %d %H:%M:%S %Y %z'),
        'navbarLinks': [
            ('dashboard', '/'),
            ('docker', '/dockman'),
            ('settings', '/settings'),
        ],
    }
    tdata.update(kwargs)
    return template(tpl, **tdata)


def staticFile(fpath):
    return static_file(fpath, _staticDir)
