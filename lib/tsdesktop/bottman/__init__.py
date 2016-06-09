from bottle import Bottle
from .utils import render, staticFile
from .views import dashboard, dockman

app = Bottle(catchall=True)


# -- static content
@app.route('/static/<fpath:path>')
def static(fpath):
    return staticFile(fpath)


# -- error 400
@app.error(400)
def error400(err):
    return render('error', err=err)


# -- error 404
@app.error(404)
def error404(err):
    return render('error', err=err)


# -- error 500
@app.error(500)
def error500(err):
    return render('error', err=err)


# -- settings
@app.route('/settings')
def settings():
    return render('settings')


# -- init views
dashboard.init(app)
dockman.init(app)
