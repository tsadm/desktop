from os import path
import bottle
from bottle import template, static_file, request, HTTPResponse
from tsdesktop import version
from time import time, strftime

_tplsDir = path.abspath(path.join(path.dirname(__file__), 'templates'))
_staticDir = path.join(_tplsDir, 'static')
bottle.TEMPLATE_PATH.insert(0, _tplsDir)


def render(tpl, **kwargs):
    tdata = {
        'appName': version.APPNAME,
        'appVersion': version._version(),
        'appVersionString': version.string(),
        'req': request,
        'now': strftime('%a %b %d %H:%M:%S %Y %z'),
        'navbarLinks': (
            ('dashboard', '/'),
            ('docker', '/dockman'),
            ('settings', '/settings'),
        ),
        'startTime': None,
        'reqTook': None,
    }
    tdata.update(kwargs)
    if tdata['startTime'] is not None:
        tdata['reqTook'] = '{:.5f}'.format(time() - tdata['startTime'])
    return template(tpl, **tdata)


def staticFile(fpath):
    return static_file(fpath, _staticDir)


def textPlain(body, status=200):
    return HTTPResponse(body, status=status, headers={'Content-Type': 'text/plain; charset=UTF-8'})
