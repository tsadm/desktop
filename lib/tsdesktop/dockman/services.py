from . import getClient


class Service:
    name = None

    def status(self):
        cli = getClient()
        s = cli.containers(all=True, filters={'name': self.containerName()})
        if s:
            return 'NONE'
        else:
            return 'error'

    def containerName(self):
        return 'tsdesktop-'+self.name


class _faked(Service):
    name = 'faked'


class _mysqld(Service):
    name = 'mysqld'


classMap = {
    'mysqld': _mysqld,
    'faked': _faked,
}
