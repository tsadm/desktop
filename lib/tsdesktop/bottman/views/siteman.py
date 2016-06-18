from time import time
from ..utils import render
from bottle import request, HTTPError, redirect, html_escape
from tsdesktop import config
from tsdesktop.siteman import sitesAll, siteGet, siteAdd, site_name_re


# -- edit site
def siteEdit(name):
    # FIXME!!
    return 'edit: '+name


# -- site info
def siteView(name):
    # FIXME!!
    site = siteGet(name)
    site.load()
    return 'view: '+html_escape(str(site))


# -- open site
def siteOpen():
    # get/check site name
    name = request.params.get('site_name', None)
    ok = site_name_re.match(name)
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
    siteAdd(name, docroot)
    # redirect to site's view
    return redirect('/sites/'+name+'/view')



# -- sites index
def sites():
    st = time()
    return render('sites', sitesAll=sitesAll(), startTime=st)


# -- init views
def init(app):
    app.route('/sites/<name>/edit', callback=siteEdit)
    app.route('/sites/<name>/view', callback=siteView)
    app.route('/sites/open', method='POST', callback=siteOpen)
    app.route('/sites', callback=sites)
