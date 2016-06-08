from bottle import Bottle
from os import path
from .render import render

app = Bottle()

@app.route('/')
def index():
    return render('index')
