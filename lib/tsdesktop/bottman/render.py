from os import path
import bottle
from bottle import template
from tsdesktop import version

bottle.TEMPLATE_PATH.insert(0, path.abspath(path.join(path.dirname(__file__), 'views')))

def render(tpl, **kwargs):
    tdata = {
        'appName': version.APPNAME,
        'appVersion': version.VERSION,
    }
    tdata.update(kwargs)
    return template(tpl, **tdata)
