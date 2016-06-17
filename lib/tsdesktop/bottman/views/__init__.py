from . import dashboard, dockman, sites

def init(app):
    dashboard.init(app)
    dockman.init(app)
    sites.init(app)
