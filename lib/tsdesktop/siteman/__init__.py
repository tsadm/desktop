import re
import sys
from os import path
from tsdesktop import config
from configparser import NoSectionError, NoOptionError


class Site:
    name = None
    docroot = None

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
        inifile = path.join(path.dirname(dpath), '.tsdesktop.ini')
        return None


# -- compile regexs
site_name_re = re.compile(r'^[a-zA-Z0-9\.\-_]+$')


# -- add site to config
def siteAdd(name, docroot):
    # load site
    site = Site(name, docroot)
    err = site.load()
    if err is not None:
        return err
    config.cfg.add_section('site:'+name)
    config.cfg.set('site:'+name, 'docroot', docroot)
    config.write()
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
                sys.stderr.write('ignore invalid site name: '+name)
                return None
            else:
                site = siteGet(name)
                rl.append(site)
    return rl
