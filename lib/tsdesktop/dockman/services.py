class Services:
    name = None

class _faked(Services):
    name = 'faked'

class _mysqld(Services):
    name = 'mysqld'

classMap = {
    'mysqld': _mysqld,
    'faked': _faked,
}
