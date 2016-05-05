import subprocess

def _cmd(argv):
    c = ["/usr/bin/env", "docker"]
    c.extend(argv)
    output = subprocess.check_output(c)
    print(output)
    return 0

def start(srv):
    print("docker start:", srv.name)
    return _cmd(["run", "--rm", "-it", srv.image])
