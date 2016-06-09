from tsdesktop.dockman import services
from ..utils import render

def view():
    sl = [s() for s in services.classMap.values()]
    return render('dashboard', dockmanServices=sl)

def init(app):
    app.route('/', callback=view)
