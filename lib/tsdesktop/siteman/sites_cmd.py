from tsdesktop import config, siteman

def add(site, docroot):
    err = siteman.siteAdd(site, docroot)
    if err is not None:
        print('add site error: %s' % err)
        return 1
    s = siteman.siteGet(site)
    if s is None:
        print('get site error!')
        return 2
    err = s.load()
    if err is not None:
        print('load site error: %s' % err)
        return 3
    config.write()
    return 0

def remove(site):
    s = siteman.siteGet(site)
    if s is None:
        print('invalid site: %s' % site)
        return 1
    err = siteman.siteRemove(site)
    if err is not None:
        print('remove site error: %s' % err)
        return 2
    return 0
