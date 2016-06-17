import time
from tsdesktop.dockman import getClient, services, checkOutput
from ..utils import render
from bottle import abort, HTTPError, redirect


# -- docker pull image
def _pullImage(cli, srvName):
    srv = services.classMap.get(srvName, None)
    if srv is None:
        return HTTPError(400, 'service name: '+srvName)
    imgInfo = srv().imageInfo()
    err = checkOutput(cli.pull(repository=imgInfo.repo(), tag=imgInfo.tag()))
    if err is not None:
        return HTTPError(500, 'docker pull: '+err)


# -- docker info
def dockman(srvName=None, action=None):
    sT = time.time()
    try:
        cli = getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)
    if action == 'pull-image':
        err = _pullImage(cli, srvName)
        if err is None:
            redirect('/dockman')
        else:
            return err
    return render('dockman', docker=cli, dockmanServices=services.classList(), startTime=sT)


# -- package init
def init(app):
    app.route('/dockman/<srvName>/<action>', callback=dockman)
    app.route('/dockman', callback=dockman)
