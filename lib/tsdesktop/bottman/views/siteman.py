from time import time
from ..utils import render
from bottle import request, HTTPError, redirect
from tsdesktop.siteman import openSite


# -- open site
def siteOpen():
    docroot = request.params.get('site_docroot', None)
    err, siteId = openSite(docroot)
    if err is not None:
        return HTTPError(400, 'could not open site: '+str(err))
    return redirect('/sites/'+siteId)


# -- sites index
def sites():
    return render('sites', startTime=time())


# -- init views
def init(app):
    app.route('/site/open', method='POST', callback=siteOpen)
    app.route('/sites', callback=sites)
