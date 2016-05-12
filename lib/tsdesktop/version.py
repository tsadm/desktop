from tsdesktop import buildinfo

VERSION = "16.05.1"

def println():
    s = "tsdesktop v{}".format(VERSION)
    if buildinfo.ID is None:
        s = "{} (devel)".format(s)
    else:
        s = "{} ({} {})".format(s, buildinfo.ID[:7], buildinfo.DATE)
    print(s)

if __name__ == '__main__':
    println()
