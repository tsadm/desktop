from tsdesktop.dockman import services
from ..utils import render

def view():
    sl = [services.classMap[k]() for k in sorted(services.classMap.keys())]
    return render('dashboard', dockmanServices=sl)

def init(app):
    app.route('/', callback=view)
