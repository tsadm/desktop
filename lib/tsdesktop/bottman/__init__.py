from bottle import Bottle, abort
from os import path
from .utils import render, staticFile
from tsdesktop import dockman
from tsdesktop.dockman import services

app = Bottle()

# -- dashboard
@app.route('/')
def index():
    sl = [s() for s in services.classMap.values()]
    return render('index', dockmanServices=sl)


# -- static content
@app.route('/static/<fpath:path>')
def static(fpath):
    return staticFile(fpath)


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
    return render('settings')


# -- docker
@app.route('/docker')
def docker():
    try:
        cli = dockman.getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)
    return render('docker', docker=cli)
