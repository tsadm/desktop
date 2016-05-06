from os import makedirs
from os.path import expanduser
from time import sleep
from tsdesktop import docker

class _service:
    name = None
    detach = True
    runArgs = []

    def action(self, act):
        self.preChecks()
        if act == "status":
            return self._status()
        elif act == "start":
            return docker.start(self)
        elif act == "stop":
            return docker.stop(self)
        else:
            print("E: invalid service action:", act)
            return 1

    def _status(self):
        print(self.name+" status")
        return 0

    def preChecks(self):
        """should be reimplemented"""
        pass

class _mysqld(_service):
    name = "mysqld"
    _datadir = "~/.cache/tsdesktop/service/mysqld/datadir"

    def __init__(self):
        self.runArgs = ["-v", self._datadir+":/var/lib/mysql"]

    def preChecks(self):
        self._datadir = expanduser(self._datadir)
        makedirs(self._datadir, mode=510, exist_ok=True)

class _httpd(_service):
    name = "httpd"
    detach = False

srvMap = {
    "mysqld": _mysqld,
    "httpd": _httpd,
}

def startEnabled(cfg):
    for name in srvMap.keys():
        if name == 'httpd':
            print('httpd will be started at the end')
            continue
        if cfg['service:'+name] and cfg['service:'+name].getboolean('enable'):
            kls = srvMap.get(name)
            kls().action('start')
        sleep(2)
    kls = srvMap.get('httpd')
    kls().action('start')
