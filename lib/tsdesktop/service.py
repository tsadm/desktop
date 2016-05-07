from os import path, makedirs
from time import sleep
from tsdesktop import docker
from tsdesktop import config


class _site:
    name = None
    docroot = None

    def __init__(self):
        self.docroot = path.join(path.abspath(path.curdir),
                                    config.cfg.get('site', 'docroot'))
        self.name = path.basename(path.dirname(self.docroot))


class _service:
    name = None
    detach = True
    runArgs = []
    site = None

    def __init__(self):
        self.site = _site()

    def action(self, act):
        if not self.preChecks():
            return 1
        if act == "status":
            return self._status()
        elif act == "start":
            return docker.start(self)
        elif act == "stop":
            return docker.stop(self)
        else:
            print("E: invalid service action:", act)
            return 2

    def _status(self):
        print(self.name+" status")
        return 0

    def preChecks(self):
        """should be reimplemented"""
        return True

    def cachePath(self, *names):
        return path.join(config.cfg.get('user', 'cachedir'),
                            'service', self.name, *names)

    def containerName(self):
        if self.detach:
            return "tsdesktop-{}".format(self.name)
        else:
            return "tsdesktop-{}-{}".format(self.name, self.site.name)

    def containerImage(self):
        return "tsdesktop/{}".format(self.name)


class _mysqld(_service):
    name = "mysqld"
    _datadir = None

    def preChecks(self):
        self._datadir = self.cachePath('datadir')
        self.runArgs = ["-v", self._datadir+":/var/lib/mysql"]
        makedirs(self._datadir, mode=510, exist_ok=True)
        return path.exists(self._datadir)


class _httpd(_service):
    name = "httpd"
    detach = False

    def preChecks(self):
        self.runArgs = [
            "-p", "127.0.0.1:33380:80",
            "-v", "{}:/var/www/html".format(self.site.docroot),
        ]
        if not path.exists(self.site.docroot):
            print("E: site docroot not found:", self.site.docroot)
            return False
        return True


srvMap = {
    "mysqld": _mysqld,
    "httpd": _httpd,
}


def startEnabled():
    for name in srvMap.keys():
        if name == 'httpd':
            print('httpd will be started at the end')
            continue
        if config.cfg.getboolean('service:'+name, 'enable'):
            kls = srvMap.get(name)
            kls().action('start')
        sleep(2)
    kls = srvMap.get('httpd')
    kls().action('start')
