import sys
from argparse import ArgumentParser
from tsdesktop import config, service

def _workCmd():
    config.read()
    stat = service.startEnabled(config.cfg)
    if stat != 0:
        return stat
    return 0

def _configCmd():
    ok = config.read()
    print("read:", " ".join(ok), end="\n\n")
    config.cfg.write(sys.stdout)

def _serviceCmd(service, action):
    from tsdesktop.service import srvMap
    kls = srvMap.get(service, None)
    if kls is None:
        print("E: invalid service:", service)
        return 2
    return kls().action(action)

def _parseArgs():
    parser = ArgumentParser(description='tsadm desktop client')
    parser.add_argument('-D', '--config', action='store_true', help='dump config')
    parser.add_argument('-S', '--service-start', metavar="service", help='start service container')
    parser.add_argument('-K', '--service-stop', metavar="service", help='stop service container')
    return parser

def main():
    parser = _parseArgs()
    args = parser.parse_args()
    if args.config:
        return _configCmd()
    elif args.service_start:
        return _serviceCmd(args.service_start, 'start')
    elif args.service_stop:
        return _serviceCmd(args.service_stop, 'stop')
    else:
        return _workCmd()
