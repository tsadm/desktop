from os import path


class Site:
    ID = None
    docroot = None

    def __init__(self, docroot):
        self.docroot = docroot
        self.ID = self._genID()

    def _genID(self):
        return self.docroot

    def load(self):
        inifile = path.join(path.dirname(self.docroot), '.tsdesktop.ini')
        print('INIFILE:', inifile)


def openSite(docroot):
    dpath = path.abspath(docroot)
    if not path.exists(dpath):
        return ('dir not found', None)
    elif not path.isdir(dpath):
        return ('not a dir', None)
    site = Site(dpath)
    site.load()
    return (site.ID, 'lalala')
