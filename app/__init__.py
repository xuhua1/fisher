
from flask import Flask
from app.models.book import db

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)

    db.init_app(app)
    return app
