from bottle import Bottle
from os import path
from .utils import render, staticFile

app = Bottle()

@app.route('/')
def index():
    return render('index')

@app.route('/static/<fpath:path>')
def static(fpath):
    return staticFile(fpath)
