from tsdesktop.dockman import getClient, services
from ..utils import render
from bottle import abort


# -- docker info
def dockman():
    try:
        cli = getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)
    images = ['lalala']
    return render('dockman', docker=cli, dockmanServices=services.classList())


def init(app):
    app.route('/dockman', callback=dockman)
