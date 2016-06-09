class Services:
    name = None

class _mysqld(Services):
    name = 'mysqld'

classMap = {
    'mysqld': _mysqld,
}
