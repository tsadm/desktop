from argparse import ArgumentParser
from tsdesktop import config, version, bottman
from tsdesktop.dockman import services_cmd


def _parseArgs():
    parser = ArgumentParser(description='tsadm desktop client')
    parser.add_argument('-V', '--version',
        action='store_true',
        help='show version and build info',
    )
    parser.add_argument('-p', '--port',
        nargs='?', type=int,
        default=3680,
        help='TCP port to bind to (default: 3680)',
    )
    parser.add_argument('-d', '--debug',
        action='store_true', help='enable debug mode')
    parser.add_argument('-C', '--config',
        action='store_true', help='dump config')
    parser.add_argument('-S', '--start', help='start container')
    parser.add_argument('-K', '--stop', help='stop container')
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

    elif args.start:
        return services_cmd.start(args.start)

    elif args.stop:
        return services_cmd.stop(args.stop)

    else:
        return bottman.app.run(host='localhost', port=args.port, debug=args.debug)
