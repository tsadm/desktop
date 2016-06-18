import re
from time import time
from ..utils import render
from bottle import request, HTTPError, redirect, html_escape
from tsdesktop import config
from tsdesktop.siteman import Site


# -- edit site
def siteEdit(name):
    # FIXME!!
    return 'edit: '+name


# -- site info
def siteView(name):
    # FIXME!!
    site = _cfgGet(name)
    site.load()
    return 'view: '+html_escape(str(site))


# -- open site
def siteOpen():
    # get/check site name
    name = request.params.get('site_name', None)
    ok = re.match(r'^[a-zA-Z0-9.-_]+$', name)
    if not ok:
        return HTTPError(400, 'invalid site name: '+name)
    # check it not exists already
    if config.cfg.has_section('site:'+name):
        return HTTPError(400, 'site already exists: '+name)
    # get docroot
    docroot = request.params.get('site_docroot', None)
    # load site
    site = Site(name, docroot)
    err = site.load()
    if err is not None:
        return HTTPError(400, 'could not open site: '+str(err))
    # add site to config and save it to disk (write)
    _cfgAdd(name, docroot)
    # redirect to site's view
    return redirect('/sites/'+name+'/view')


# -- add site to config
def _cfgAdd(name, docroot):
    config.cfg.add_section('site:'+name)
    config.cfg.set('site:'+name, 'docroot', docroot)
    config.write()


# -- get site from config
def _cfgGet(name):
    docroot = config.cfg.get('site:'+name, 'docroot')
    if docroot is not None:
        return Site(name, docroot)
    return None


# -- sites index
def sites():
    return render('sites', startTime=time())


# -- init views
def init(app):
    app.route('/sites/<name>/edit', callback=siteEdit)
    app.route('/sites/<name>/view', callback=siteView)
    app.route('/sites/open', method='POST', callback=siteOpen)
    app.route('/sites', callback=sites)
