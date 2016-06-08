from bottle import Bottle, abort
from os import path
from .utils import render, staticFile
from tsdesktop import dockman

app = Bottle()


@app.route('/')
def index():
    tdata = {
        'dockmanServices': [
            {'name': 'mysqld'},
            {'name': 'faked'},
        ],
    }
    return render('index', **tdata)


@app.route('/static/<fpath:path>')
def static(fpath):
    return staticFile(fpath)


@app.error(404)
def error404(err):
    return render('error', err=err)


@app.error(500)
def error500(err):
    return render('error', err=err)


@app.route('/settings')
def settings():
    return render('settings')


@app.route('/docker')
def docker():
    try:
        cli = dockman.getClient()
        cli.ping()
    except Exception as e:
        abort(500, e)
    return render('docker', docker=cli)
