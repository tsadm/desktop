import re
import sys
from os import path
from tsdesktop import config
from tsdesktop.dockman import services
from configparser import NoSectionError, NoOptionError


class Site:
    name = None
    docroot = None
    webserver = None

    def __init__(self, name, docroot):
        self.name = name
        self.docroot = docroot

    def __str__(self):
        return "<Site: {}>".format(self.name)

    def load(self):
        dpath = path.abspath(self.docroot)
        if not path.exists(dpath):
            return 'path not found'
        elif not path.isdir(dpath):
            return 'not a dir'
        return None

    def _initws(self):
        if self.webserver is None:
            s = config.cfg.get('site:'+self.name, 'webserver')
            k = services.classMap.get(s)
            self.webserver = k(site=self.name)

    def status(self):
        self._initws()
        return self.webserver.status()

    def start(self):
        self._initws()
        self.webserver.volAdd(self.docroot, '/var/www/html')
        return self.webserver.start()

    def stop(self):
        self._initws()
        return self.webserver.stop()



# -- compile regexs
site_name_re = re.compile(r'^[a-zA-Z0-9\.\-_]+$')


# -- check if docroot is already in use by a site
def _dupDocroot(dpath):
    for s in sitesAll():
        if s.docroot == dpath:
            return "{} registered by {}".format(dpath, s.name)
    return None


# -- add site to config
def siteAdd(name, docroot):
    if config.cfg.has_section('site:'+name):
        return 'site already exists'

    err = _dupDocroot(docroot)
    if err is not None:
        return err

    config.cfg.add_section('site:'+name)
    config.cfg.set('site:'+name, 'docroot', docroot)
    return None


# -- get site from config
def siteGet(name):
    try:
        docroot = config.cfg.get('site:'+name, 'docroot')
    except NoSectionError:
        return None
    except NoOptionError:
        return None
    return Site(name, docroot)


# -- get all sites from config
def sitesAll():
    rl = list()
    for sect in config.cfg.sections():
        if sect.startswith('site:'):
            name = ':'.join(sect.split(':')[1:])
            ok = site_name_re.match(name)
            if not ok:
                # FIXME: print/log a message about the invalid site name
                return None
            else:
                site = siteGet(name)
                err = site.load()
                if err is None:
                    rl.append(site)
                # FIXME: else log a message at least
    return rl


def sitesRunning():
    """returns list of running sites"""
    r = list()
    for s in sitesAll():
        if s.status() == 'running':
            r.append(s)
    return r
