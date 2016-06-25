from . import getClient
from docker.errors import APIError


class ImageInfo:
    name = None
    status = None

    def __init__(self, name, info=None, missing=False, error=False):
        self.name = name
        if error:
            self.status = 'error'
        elif missing:
            self.status = 'missing'
        elif info:
            self.status = 'ok'

    def repo(self):
        return self.name.split(':')[0]

    def tag(self):
        try:
            return self.name.split(':')[1]
        except IndexError:
            return ''


class Service:
    name = None
    dedicated = False
    site = None
    container = None

    def __init__(self, site=None):
        self.site = site

    def __str__(self):
        return "<Service: {}>".format(self._contName())

    def __repr__(self):
        return str(self)

    def status(self):
        cli = getClient()
        l = cli.containers(all=True, filters={'name': self._contName()})
        for s in l:
            print(type(s), s)
            if '/%s' % self._contName() in s['Names']:
                stat = s.get('Status', None)
                if stat is None:
                    return 'error'
                elif stat.startswith('Up'):
                    return 'running'
                elif stat.startswith('Exited'):
                    return 'exit'
                else:
                    return 'error'
        else:
            return ''

    def _contName(self):
        n = 'tsdesktop-'+self.name
        if self.site is not None:
            n = n+'-'+self.site
        return n

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

    def _container(self):
        cli = getClient()
        return cli.create_container(
            name=self._contName(),
            image=self._imgName(),
        )

    def start(self):
        cli = getClient()
        stat = self.status()
        if stat == 'exit':
            cli.remove_container(container=self._contName(), v=True)
        elif stat == 'running':
            return self._contName()+': already running'
        cont = self._container()
        err = cli.start(container=cont.get('Id'))
        if err is not None:
            return self._contName()+': error - '+str(err)
        self.container = cont
        return None

    def stop(self):
        cli = getClient()
        stat = self.status()
        if stat == 'exit':
            cli.remove_container(container=self._contName(), v=True)
            self.container = None
            return None
        elif stat == 'running':
            try:
                cli.stop(self._contName())
            except APIError as e:
                return '%s: %s' % (self._contName(), e)
            cli.remove_container(container=self._contName(), v=True)
            self.container = None
            return None
        return self._contName()+': not running'


class _httpd(Service):
    name = 'httpd'
    dedicated = True


class _mysqld(Service):
    name = 'mysqld'


classMap = {
    'mysqld': _mysqld,
    'httpd': _httpd,
}


def classList():
    return [classMap[k]() for k in sorted(classMap.keys())]
