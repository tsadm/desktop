from tsdesktop.dockman import getClient, services
from ..utils import render
from bottle import abort, HTTPError


# -- docker pull image
def _pullImage(cli, srvName):
    # FIXME!
    srv = services.classMap.get(srvName, None)
    if srv is None:
        return HTTPError(400, 'service name: '+srvName)
    imgInfo = srv().imageInfo()
    cli.pull(repository=imgInfo.repository(), tag=imgInfo.tag(), stream=False)
    return None


# -- docker info
def dockman(srvName=None, action=None):
    try:
        cli = getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)
    if action == 'pull-image':
        err = _pullImage(cli, srvName)
        if err is not None:
            return err
    return render('dockman', docker=cli, dockmanServices=services.classList())


# -- package init
def init(app):
    app.route('/dockman/<srvName>/<action>/', callback=dockman)
    app.route('/dockman', callback=dockman)
