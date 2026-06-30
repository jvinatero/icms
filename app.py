from flask import Flask
from config import Config
from extensions import db, migrate

from blueprints.dashboard import dashboard_bp
from blueprints.groups import groups_bp

import models


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(groups_bp)

    return app