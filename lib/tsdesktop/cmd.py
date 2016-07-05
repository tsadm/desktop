from argparse import ArgumentParser
from tsdesktop import config, version, bottman
from tsdesktop.dockman import services_cmd
from tsdesktop.siteman import sites_cmd


def _parseArgs():
    parser = ArgumentParser(description='tsadm desktop client')
    parser.add_argument('-V', '--version',
        help='show version and build info', action='store_true')
    parser.add_argument('-d', '--debug',
        action='store_true', help='enable debug mode')

    parser.add_argument('-p', '--port',
        help='TCP port to bind to (default: 3680)', nargs='?',
        type=int, default=3680, metavar='port')
    parser.add_argument('-C', '--config',
        action='store_true', help='dump config')

    parser.add_argument('-S', '--start',
        help='start container', metavar='service')
    parser.add_argument('-K', '--stop',
        help='stop container', metavar='service')
    parser.add_argument('-R', '--restart',
        help='restart container', metavar='service')
    parser.add_argument('-L', '--login',
        help='login to container', metavar='service')

    parser.add_argument('--dbserver',
        help='database server (default: mysqld)', default='mysqld', metavar='name')
    parser.add_argument('-J', '--importdb',
        help='database import reading from stdin', metavar='dbname')

    parser.add_argument('-s', '--site',
        help='site name', metavar='name', default=None)
    parser.add_argument('--add',
        help='add site docroot/public_html to configuration', metavar='docroot')
    parser.add_argument('--remove',
        action='store_true', help='remove site from configuration')
    return parser


def main():
    version.println()
    cfgFile = config.read()
    parser = _parseArgs()
    args = parser.parse_args()

    if args.config:
        print("read: {}".format(cfgFile))
        return config.cmd()

    elif args.version:
        return 0

    elif args.restart:
        return services_cmd.restart(args.restart, args.site)

    elif args.start:
        return services_cmd.start(args.start, args.site)

    elif args.stop:
        return services_cmd.stop(args.stop, args.site)

    elif args.login:
        return services_cmd.login(args.login, args.site)

    elif args.importdb:
        return services_cmd.importDB(args.dbserver, args.importdb)

    elif args.site:
        if args.add:
            return sites_cmd.add(args.site, args.add)
        elif args.remove:
            return sites_cmd.remove(args.site)

    else:
        return bottman.app.run(host='localhost', port=args.port, debug=args.debug)
