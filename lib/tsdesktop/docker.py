import os
from subprocess import Popen

def _cmd(srv, args, wait=True):
    c = ["/usr/bin/env", "docker"]
    c.extend(args)
    pid = Popen(c).pid
    print("docker run:", " ".join(c), "PID:", pid)
    if wait:
        _, stat = os.wait()
        return stat
    else:
        return pid

def start(srv):
    img = "tsdesktop/"+srv.name
    print("docker start:", srv.name, img)
    args = ["run", "-d", "--name="+img.replace("/", "-")]
    args.extend(srv.runArgs)
    args.append(img)
    return _cmd(srv, args, wait=False)

def stop(srv):
    container = "tsdesktop-"+srv.name
    print("docker stop:", srv.name)
    stat = _cmd(srv, ["stop", container])
    if stat != 0:
        return stat
    print("docker remove:", srv.name)
    return _cmd(srv, ["rm", "-v", container])
