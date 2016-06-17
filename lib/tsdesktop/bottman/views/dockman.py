import time
from tsdesktop.dockman import getClient, services, checkOutput
from ..utils import render
from bottle import abort, HTTPError, redirect


# -- docker start service container
def _startService(cli, srvName):
    cls = services.classMap.get(srvName, None)
    if cls is None:
        return HTTPError(400, 'service name: '+srvName)
    err = cls().start()
    if err is not None:
        return HTTPError(500, 'docker start: '+err)
    return None


# -- docker pull image
def _pullImage(cli, srvName):
    srv = services.classMap.get(srvName, None)
    if srv is None:
        return HTTPError(400, 'service name: '+srvName)
    imgInfo = srv().imageInfo()
    err = checkOutput(cli.pull(repository=imgInfo.repo(), tag=imgInfo.tag()))
    if err is not None:
        return HTTPError(500, 'docker pull: '+err)


# -- docker action manager
def dockman(srvName=None, action=None):
    err = None
    sT = time.time()
    try:
        cli = getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)

    if action is None:
        return render('dockman', docker=cli, dockmanServices=services.classList(), startTime=sT)

    elif action == 'pull-image':
        err = _pullImage(cli, srvName)

    elif action == 'start':
        err = _startService(cli, srvName)

    else:
        err = HTTPError(400, 'bad request')

    if err is None:
        redirect('/dockman')
    else:
        return err


# -- package init
def init(app):
    app.route('/dockman/<srvName>/<action>', callback=dockman)
    app.route('/dockman', callback=dockman)
