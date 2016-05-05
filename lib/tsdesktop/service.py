from tsdesktop import docker

class _service:
    name = None
    image = None

    def action(self, act):
        if act == "status":
            return self._status()
        elif act == "start":
            return docker.start(self)
        else:
            print("E: invalid service action")
            return 1

    def _status(self):
        print(self.name +" "+ self.image +" "+ "status")
        return 0

class _mysqlSrv(_service):
    name = "mysql"
    image = "tsdesktop/mysqld"

cmdMap = {
    "mysql": _mysqlSrv,
}
