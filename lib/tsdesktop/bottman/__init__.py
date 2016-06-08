from bottle import Bottle
from os import path
from .utils import render, staticFile

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


@app.route('/settings')
def index():
    return render('settings')
