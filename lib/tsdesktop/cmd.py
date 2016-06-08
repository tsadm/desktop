from argparse import ArgumentParser
from tsdesktop import config, service, version, cmd_mysql, bottman


def _workCmd():
    stat = service.startEnabled()
    if stat != 0:
        return stat
    return 0


def _parseArgs():
    parser = ArgumentParser(description='tsadm desktop client')
    parser.add_argument('-V', '--version', action='store_true', help='show version and build info')
    parser.add_argument('--http', nargs='?', type=int, const=3680, metavar="PORT", help='start web interface (default port: 3680)')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug mode')
    parser.add_argument('-D', '--config', action='store_true', help='dump config')
    parser.add_argument('-S', '--service-start', metavar="service", help='start service container')
    parser.add_argument('-K', '--service-stop', metavar="service", help='stop service container')
    parser.add_argument('-L', '--service-login', metavar="service", help='login to a service container')
    parser.add_argument('-w', '--work', action='store_true', help='work on current site installation')
    parser.add_argument('--sql-import', metavar="file.sql", help='import sql file into site database')
    return parser


def main():
    version.println()
    config.read()
    parser = _parseArgs()
    args = parser.parse_args()

    if args.http:
        return bottman.app.run(host='localhost', port=args.http, debug=args.debug)

    elif args.config:
        return config.cmd()

    elif args.service_start:
        return service.cmd(args.service_start, 'start')

    elif args.service_stop:
        return service.cmd(args.service_stop, 'stop')

    elif args.service_login:
        return service.cmd(args.service_login, 'login')

    elif args.work:
        return _workCmd()

    elif args.version:
        #~ version.println()
        return 0

    elif args.sql_import:
        return cmd_mysql.importFile(args.sql_import)

    else:
        parser.print_help()
        return 1
