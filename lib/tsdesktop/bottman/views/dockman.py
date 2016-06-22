import time
from tsdesktop.dockman import getClient, services, checkOutput
from ..utils import render, textPlain
from bottle import abort, HTTPError, redirect


# -- docker start service container
def _startService(srvc):
    err = srvc.start()
    if err is not None:
        return textPlain(err, 400)
    return None


# -- docker stop service container
def _stopService(srvc):
    err = srvc.stop()
    if err is not None:
        return textPlain(err, 400)
    return None


# -- docker pull image
def _pullImage(cli, srvc):
    imgInfo = srvc.imageInfo()
    err = checkOutput(cli.pull(repository=imgInfo.repo(), tag=imgInfo.tag()))
    if err is not None:
        return HTTPError(500, 'docker pull: '+err)


# -- docker action manager
def view(service=None, action=None):
    err = None
    sT = time.time()
    try:
        cli = getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)

    srvc = None
    if action is not None:
        klass = services.classMap.get(service, None)
        if klass is None:
            return HTTPError(400, 'invalid service: '+str(service))
        srvc = klass()

    if action is None:
        return render('dockman',
            docker=cli, dockmanServices=services.classList(), startTime=sT)

    elif action == 'pull-image':
        err = _pullImage(cli, srvc)

    elif action == 'start':
        err = _startService(srvc)

    elif action == 'stop':
        err = _stopService(srvc)

    else:
        err = textPlain('bad request', 400)

    if err is None:
        redirect('/dockman')
    else:
        return err


# -- package init
def init(app):
    app.route('/dockman/<service>/<action>', callback=view)
    app.route('/dockman', callback=view)
