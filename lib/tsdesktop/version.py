from tsdesktop import buildinfo

VERSION = "16.05"

def println():
    s = "tsdesktop v{}".format(VERSION)
    if not buildinfo.ID is None:
        s = "{} ({} {})".format(s, buildinfo.ID[:7], buildinfo.DATE)
    print(s)

if __name__ == '__main__':
    println()
