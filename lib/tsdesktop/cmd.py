from argparse import ArgumentParser
from tsdesktop import config, version, bottman


def _parseArgs():
    parser = ArgumentParser(description='tsadm desktop client')
    parser.add_argument('-V', '--version', action='store_true', help='show version and build info')
    parser.add_argument('--http', nargs='?', type=int, const=3680, metavar="PORT", help='start web interface (default port: 3680)')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug mode')
    parser.add_argument('-D', '--config', action='store_true', help='dump config')
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

    elif args.version:
        return 0

    else:
        parser.print_help()
        return 1
