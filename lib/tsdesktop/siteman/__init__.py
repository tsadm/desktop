from os import path


class Site:
    name = None
    docroot = None

    def __init__(self, name, docroot):
        self.name = name
        self.docroot = docroot

    def load(self):
        dpath = path.abspath(self.docroot)
        if not path.exists(dpath):
            return 'path not found'
        elif not path.isdir(dpath):
            return 'not a dir'
        inifile = path.join(path.dirname(dpath), '.tsdesktop.ini')
        return None
