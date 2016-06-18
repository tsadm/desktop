from os import path


class Site:
    name = None
    docroot = None

    def __init__(self, name, docroot):
        self.name = name
        self.docroot = docroot

    def load(self):
        inifile = path.join(path.dirname(self.docroot), '.tsdesktop.ini')


def openSite(name, docroot):
    dpath = path.abspath(docroot)
    if not path.exists(dpath):
        return 'path not found'
    elif not path.isdir(dpath):
        return 'not a dir'
    site = Site(name, dpath)
    site.load()
    return site
