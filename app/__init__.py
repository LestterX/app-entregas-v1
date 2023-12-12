import flask 
from .static.database.database_controller import *

create_database()

def start_app():
    app = flask.Flask(__name__)
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app
