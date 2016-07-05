import os
from os import path
from . import getClient
from docker.errors import APIError
from tsdesktop import config


class ImageInfo(object):
    """docker image information and status"""
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
        """returns image repository part of the name (repo:tag)"""
        return self.name.split(':')[0]

    def tag(self):
        """returns image tag part of the name (repo:tag)"""
        try:
            return self.name.split(':')[1]
        except IndexError:
            return ''


class Service(object):
    """manages docker images and containers for services"""
    name = None
    dedicated = False
    site = None
    container = None
    containerName = None
    ports = []
    volumes = []
    hostConfig = {}
    environ = {}
    URI = None
    URIDesc = None

    def __init__(self, site=None):
        self.site = site
        self.containerName = self._contName()
        self._defaultEnviron()

    def __str__(self):
        return '<Service: %s>' % self.containerName

    def __repr__(self):
        return str(self)

    def _defaultEnviron(self):
        """sets common environment variables for all containers"""
        self.environ.update({
            'TSDESKTOP_UID': os.getuid(),
            'TSDESKTOP_GID': os.getgid(),
        })

    def status(self):
        """returns container status ('error'|'running'|'exit'|'')"""
        cli = getClient()
        l = cli.containers(all=True, filters={'name': self.containerName})
        for s in l:
            if '/%s' % self.containerName in s.get('Names', []):
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
        """builds and returns container name, based on the service name"""
        n = 'tsdesktop-'+self.name
        if self.site is not None:
            n = n+'-'+self.site
        return n

    def imageInfo(self):
        """returns service image information (ImageInfo)"""
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
        """builds and returns image name, based on the service name"""
        return 'tsadm/desktop:'+self.name

    def _rmContainer(self, cli):
        """removes docker container"""
        cli.remove_container(container=self.containerName, v=True)
        self.container = None

    def _mkContainer(self):
        """creates docker container"""
        cli = getClient()
        self.container = cli.create_container(
            name=self.containerName,
            image=self._imgName(),
            ports=self.ports,
            volumes=self.volumes,
            environment=self.environ,
            host_config=cli.create_host_config(**self.hostConfig),
        )

    def start(self):
        """starts service container"""
        cli = getClient()
        stat = self.status()
        if stat in ('exit', 'error'):
            self._rmContainer(cli)
        elif stat == 'running':
            return self.containerName+': already running'
        try:
            self._mkContainer()
            err = cli.start(container=self.container.get('Id'))
            if err is not None:
                return self.containerName+': error - '+str(err)
        except APIError as e:
            return '%s - %s' % (self.containerName, e.explanation.decode())
        return None

    def stop(self):
        """stops service container"""
        cli = getClient()
        stat = self.status()
        if stat == 'exit':
            self._rmContainer(cli)
            return None
        elif stat == 'running':
            try:
                cli.stop(self.containerName)
            except APIError as e:
                return '%s: %s' % (self.containerName, e)
            self._rmContainer(cli)
            return None
        return self.containerName+': not running'

    def run(self, cmd):
        cli = getClient()
        proc = cli.exec_create(container=self.containerName, cmd=cmd)
        return cli.exec_start(proc).decode()

    def volAdd(self, orig, dest, mode='rw'):
        """adds a volume to the docker container"""
        if self.container is not None:
            raise RuntimeError('volAdd called after container was created')
        self.volumes.append(dest)
        if not 'binds' in self.hostConfig.keys():
            self.hostConfig['binds'] = {}
        self.hostConfig['binds'][orig] = {
            'bind': dest,
            'mode': mode,
        }

    def cachePath(self, *args):
        p = path.expanduser(config.cfg.get('user', 'cachedir'))
        return path.abspath(path.join(p, self.name, *args))


class _httpd(Service):
    """http (apache2) service manager"""
    name = 'httpd'
    dedicated = True
    ports = [80, 443]
    hostConfig = {
        'port_bindings': {
            80: ('127.0.0.1', 4080),
            443: ('127.0.0.1', 4443),
        },
    }
    URI = 'http://localhost:4080/'

    def start(self):
        dbserver = config.cfg.get('site:'+self.site, 'dbserver')
        k = classMap.get(dbserver, None)
        if k is not None:
            dbs = k()
            if dbs.status() != 'running':
                return '%s service should be started first (%s)' % (dbserver, dbs.status())
            err = dbs.createDB('%sdb' % self.site, self.site, self.containerName)
            if err:
                return err
        self.environ['TSDESKTOP_SITE'] = self.site
        return super(_httpd, self).start()


class _mysqld(Service):
    """mysql service container manager"""
    name = 'mysqld'
    ports = [80, 3306]
    hostConfig = {
        'port_bindings': {
            80: ('127.0.0.1', 4980),
            3306: ('127.0.0.1', 4936),
        },
    }
    URI = 'http://localhost:4980/phpmyadmin'
    URIDesc = 'login as tsdesktop:tsdesktop'

    def start(self):
        self.volAdd(self.cachePath('datadir'), '/var/lib/mysql')
        self.volAdd(self.cachePath('upload'), '/var/tmp/upload')
        return super(_mysqld, self).start()

    def createDB(self, dbname, user, host):
        return self.run('/opt/tsdesktop/mysqld.createdb %s %s %s' % (dbname, user, host))


classMap = {
    'mysqld': _mysqld,
    'httpd': _httpd,
}


def classList():
    return [classMap[k]() for k in sorted(classMap.keys())]
