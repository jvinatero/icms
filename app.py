from flask import Flask, request

from config import Config
from extensions import db, migrate

from blueprints.dashboard import dashboard_bp
from blueprints.groups import groups_bp
from blueprints.areas import areas_bp
from blueprints.assignments import assignments_bp
from blueprints.monthly_schedule import monthly_schedule_bp
from blueprints.reports import reports_bp

import models


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(groups_bp)
    app.register_blueprint(areas_bp)
    app.register_blueprint(assignments_bp)
    app.register_blueprint(monthly_schedule_bp)
    app.register_blueprint(reports_bp)

    @app.context_processor
    def inject_active_page():

        return {
            "active_page": request.endpoint or ""
        }

    return app