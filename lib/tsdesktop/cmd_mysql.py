from os.path import abspath
from subprocess import PIPE
from tsdesktop import service, docker

def importFile(filename):
    fpath = abspath(filename)
    print(fpath)
    srv = service.new("mysqld")
    with open(fpath, 'rb') as fh:
        proc = docker.exec(srv, ["mysql", "-B", srv.site.dbName()], wait=False, stdin=fh)
        proc.communicate()
        fh.close()
        return proc.returncode
    return 128
