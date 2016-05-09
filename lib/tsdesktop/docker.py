import os
from subprocess import Popen


def _cmd(srv, args, wait=True):
    c = ["docker"]
    c.extend(args)
    print("docker cmd:", " ".join(c))
    proc = Popen(c)
    print("docker cmd PID:", proc.pid)
    if wait:
        return proc.wait()
    else:
        return proc


def start(srv, docker_cmd=None):
    img = srv.containerImage()
    print("docker start:", srv.name, img)
    args = ["run",
        "--name={}".format(srv.containerName()),
        "--hostname={}".format(srv.containerName())]
    detach = ["-d"]
    if not srv.detach:
        detach = ["--rm", "-it"]
    args.extend(detach)
    args.extend(srv.runArgs)
    args.extend([
        "-e", "TSDESKTOP_UID={}".format(os.getuid()),
        "-e", "TSDESKTOP_GID={}".format(os.getgid()),
        "-e", "TSDESKTOP_SITE={}".format(srv.site.name),
    ])
    args.append(img)
    if docker_cmd is not None:
        args.extend(docker_cmd.split())
    if srv.detach:
        return _cmd(srv, args, wait=False)
    else:
        proc = _cmd(srv, args, wait=False)
        proc.communicate()
        return proc.returncode


def stop(srv):
    container = "tsdesktop-"+srv.name
    print("docker stop:", srv.name)
    stat = _cmd(srv, ["stop", container])
    if stat != 0:
        return stat
    print("docker remove:", srv.name)
    return _cmd(srv, ["rm", "-v", container])


def login(srv):
    srv.detach = False
    return start(srv, '/bin/bash -l')


def exec(srv, command):
    args = ["exec", srv.containerName()]
    args.extend(command)
    return _cmd(srv, args)
