from time import time
from ..utils import render, textPlain
from bottle import request, HTTPError, redirect, html_escape
from tsdesktop import config
from tsdesktop.siteman import sitesAll, siteGet, siteAdd, site_name_re


# -- remove site
def siteRemove(name):
    site = siteGet(name)
    if site is None:
        return textPlain('site not found: '+name, 404)
    config.cfg.remove_section('site:'+name)
    config.write()
    return textPlain('site removed: '+name)


# -- edit site
def siteEdit(name):
    # FIXME!!
    st = time()
    site = siteGet(name)
    if site is None:
        return HTTPError(404, 'site not found: '+name)
    err = site.load()
    if err is not None:
        return HTTPError(400, 'could not load site: '+str(err))
    return render('site_edit', site=site, startTime=st)


# -- site info
def siteView(name):
    st = time()
    site = siteGet(name)
    if site is None:
        return HTTPError(404, 'site not found: '+name)
    err = site.load()
    if err is not None:
        return HTTPError(400, 'could not load site: '+str(err))
    return render('site_view', site=site, startTime=st)


# -- open site
def siteOpen(name=None, docroot=None):
    # get/check site name
    if name is None:
        name = request.params.get('site_name', None)
    ok = site_name_re.match(name)
    if not ok:
        return HTTPError(400, 'invalid site name: '+name)
    # check it not exists already
    if config.cfg.has_section('site:'+name):
        return HTTPError(400, 'site already exists: '+name)
    # get docroot
    if docroot is None:
        docroot = request.params.get('site_docroot', None)
    # add site to config and save it to disk
    err = siteAdd(name, docroot)
    if err is not None:
        return HTTPError(400, 'could not add site: '+str(err))
    # redirect to site's view
    return redirect('/siteman/'+name+'/view')



# -- add site / all sites status
def sites():
    st = time()
    return render('siteman', sitesAll=sitesAll(), startTime=st)


# -- init views
def init(app):
    app.route('/siteman/<name>/remove', method='POST', callback=siteRemove)
    app.route('/siteman/<name>/edit', callback=siteEdit)
    app.route('/siteman/<name>/view', callback=siteView)
    app.route('/siteman/open', method='POST', callback=siteOpen)
    app.route('/siteman', callback=sites)
