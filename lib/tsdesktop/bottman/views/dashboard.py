from time import time
from tsdesktop.dockman import services
from ..utils import render

def view():
    return render('dashboard', dockmanServices=services.classList(), startTime=time())

def init(app):
    app.route('/', callback=view)
