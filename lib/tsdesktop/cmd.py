from argparse import ArgumentParser
from tsdesktop import config, version, bottman


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

    else:
        return bottman.app.run(host='localhost', port=args.port, debug=args.debug)
