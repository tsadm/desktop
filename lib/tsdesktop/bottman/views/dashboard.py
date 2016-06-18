from time import time
from tsdesktop.dockman import services
from tsdesktop.siteman import sitesAll
from ..utils import render

def view():
    st = time()
    return render('dashboard',
        dockmanServices=services.classList(),
        sitesAll=sitesAll(),
        startTime=st,
    )

def init(app):
    app.route('/', callback=view)
