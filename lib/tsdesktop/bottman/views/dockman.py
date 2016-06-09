from tsdesktop.dockman import getClient
from ..utils import render
from bottle import abort


# -- docker info
def dockerInfo():
    try:
        cli = getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)
    return render('docker', docker=cli)


def init(app):
    app.route('/docker', callback=dockerInfo)
