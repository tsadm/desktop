from . import getClient

class ImageInfo:
    name = None
    status = 'NONE'

    def __init__(self, name, info=None, missing=False, error=False):
        self.name = name
        if error:
            self.status = 'error'
        elif missing:
            self.status = 'missing'
        elif info:
            self.status = 'ok'


class Service:
    name = None
    dedicated = False

    def status(self):
        cli = getClient()
        s = cli.containers(all=True, filters={'name': self._contName()})
        if s:
            return 'running'
        else:
            return 'error'

    def _contName(self):
        return 'tsdesktop-'+self.name

    def imageInfo(self):
        imgName = self._imgName()
        cli = getClient()
        il = cli.images(name='tsadm/desktop')
        if il:
            for s in il:
                rt = s.get('RepoTags', [])
                if imgName in rt:
                    return ImageInfo(imgName, info=s)
            return ImageInfo(imgName, missing=True)
        else:
            return ImageInfo(imgName, error=True)

    def _imgName(self):
        return 'tsadm/desktop:'+self.name


class _httpd(Service):
    name = 'httpd'
    dedicated = True


class _mysqld(Service):
    name = 'mysqld'


_clsMap = {
    'mysqld': _mysqld,
    'httpd': _httpd,
}


def classList():
    return [_clsMap[k]() for k in sorted(_clsMap.keys())]
