import re
from time import time
from ..utils import render
from bottle import request, HTTPError, redirect
from tsdesktop.siteman import openSite


# -- site info
def siteView(name):
    return name


# -- open site
def siteOpen():
    name = request.params.get('site_name', None)
    ok = re.match(r'^[a-zA-Z0-9.-_]+$', name)
    if not ok:
        return HTTPError(400, 'invalid site name: '+name)
    docroot = request.params.get('site_docroot', None)
    err = openSite(name, docroot)
    if err is not None:
        return HTTPError(400, 'could not open site: '+str(err))
    return redirect('/site/'+name+'/view')


# -- sites index
def sites():
    return render('sites', startTime=time())


# -- init views
def init(app):
    app.route('/site/<name>/view', callback=siteView)
    app.route('/site/open', method='POST', callback=siteOpen)
    app.route('/sites', callback=sites)
