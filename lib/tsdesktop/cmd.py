import sys
from argparse import ArgumentParser
from tsdesktop import config

def _serviceCmd(service, action):
    from tsdesktop.service import srvMap
    kls = srvMap.get(service, None)
    if kls is None:
        print("E: invalid service:", service)
        return 2
    srv = kls()
    return srv.action(action)

def _parseArgs():
    parser = ArgumentParser(description='tsadm desktop client')
    parser.add_argument('--service-start', metavar="service", help='start service container')
    parser.add_argument('--service-stop', metavar="service", help='stop service container')
    return parser

def main():
    parser = _parseArgs()
    args = parser.parse_args()
    if args.service_start:
        return _serviceCmd(args.service_start, 'start')
    elif args.service_stop:
        return _serviceCmd(args.service_stop, 'stop')
    else:
        parser.print_help()
        return 1
    return 0
