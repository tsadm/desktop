import os
from subprocess import Popen

def _cmd(srv, args, wait=True):
    c = ["docker"]
    c.extend(args)
    print("docker run:", " ".join(c))
    proc = Popen(c)
    print("docker run PID:", proc.pid)
    if wait:
        return proc.wait()
    else:
        return proc

def start(srv):
    img = "tsdesktop/"+srv.name
    print("docker start:", srv.name, img)
    args = ["run", "--name="+img.replace("/", "-")]
    detach = ["-d"]
    if not srv.detach:
        detach = ["--rm", "-it"]
    args.extend(detach)
    args.append(img)
    if srv.detach:
        return _cmd(srv, args, wait=False)
    else:
        proc = _cmd(srv, args, wait=False)
        proc.communicate()

def stop(srv):
    container = "tsdesktop-"+srv.name
    print("docker stop:", srv.name)
    stat = _cmd(srv, ["stop", container])
    if stat != 0:
        return stat
    print("docker remove:", srv.name)
    return _cmd(srv, ["rm", "-v", container])
