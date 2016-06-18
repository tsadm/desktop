from . import dashboard, dockman, siteman

def init(app):
    dashboard.init(app)
    dockman.init(app)
    siteman.init(app)
