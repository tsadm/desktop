from tsdesktop.dockman import services
from ..utils import render

def view():
    return render('dashboard', dockmanServices=services.classList())

def init(app):
    app.route('/', callback=view)
