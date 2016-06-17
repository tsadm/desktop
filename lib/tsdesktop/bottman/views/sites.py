from time import time
from ..utils import render

def sites():
    return render('sites', startTime=time())

def init(app):
    app.route('/sites', callback=sites)
