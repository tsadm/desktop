from os import makedirs
from os.path import expanduser
from tsdesktop import docker

class _service:
    name = None
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

srvMap = {
    "mysqld": _mysqld,
    "httpd": _httpd,
}
