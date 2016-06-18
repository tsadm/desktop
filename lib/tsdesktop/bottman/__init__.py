from bottle import Bottle
from .utils import render, staticFile
from . import views
from time import time
from platform import python_version, system, machine
from bottle import __version__ as bottle_version
from docker import version as dockerpy_version
from io import StringIO


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


# -- error 405
@app.error(405)
def error405(err):
    return render('error', err=err)


# -- error 500
@app.error(500)
def error500(err):
    return render('error', err=err)


# -- settings
@app.route('/settings')
def settings():
    from tsdesktop.config import cfg, filepath
    buf = StringIO()
    cfg.write(buf)
    buf.seek(0, 0)
    return render('settings', config=buf, filePath=filepath)


# -- about
@app.route('/about')
def about():
    return render('about',
        pythonVersion='{} ({} {})'.format(python_version(), system(), machine()),
        bottleVersion=bottle_version,
        dockerpyVersion=dockerpy_version,
        startTime=time(),
    )


# -- init views
views.init(app)
