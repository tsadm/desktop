class Service:
    name = None

    def status(self):
        return 'NONE'


class _faked(Service):
    name = 'faked'


class _mysqld(Service):
    name = 'mysqld'


classMap = {
    'mysqld': _mysqld,
    'faked': _faked,
}
