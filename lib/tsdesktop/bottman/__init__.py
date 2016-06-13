from bottle import Bottle
from .utils import render, staticFile
from .views import dashboard, dockman

app = Bottle(catchall=True)


# -- static content
@app.route('/static/<fpath:path>')
def static(fpath):
    return staticFile(fpath)


# -- error 400
@app.error(400)
def error400(err):
    return render('error', err=err)


# -- error 404
@app.error(404)
def error404(err):
    return render('error', err=err)


# -- error 500
@app.error(500)
def error500(err):
    return render('error', err=err)


# -- settings
@app.route('/settings')
def settings():
    from tsdesktop.config import cfg
    from io import StringIO
    buf = StringIO()
    cfg.write(buf)
    buf.seek(0, 0)
    return render('settings', config=buf)


# -- about
@app.route('/about')
def about():
    from sys import version as python_version
    from bottle import __version__ as bottle_version
    from docker import version as dockerpy_version
    return render('about',
        bottleVersion=bottle_version,
        pythonVersion=python_version,
        dockerpyVersion=dockerpy_version,
    )


# -- init views
dashboard.init(app)
dockman.init(app)
