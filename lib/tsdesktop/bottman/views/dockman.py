from tsdesktop.dockman import getClient
from ..utils import render
from bottle import abort


# -- docker info
def dockman():
    try:
        cli = getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)
    return render('dockman', docker=cli)


def init(app):
    app.route('/dockman', callback=dockman)
