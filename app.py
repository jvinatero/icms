from flask import Flask
from config import Config
from extensions import db, migrate
from blueprints.groups import groups_bp

import models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(groups_bp)

    @app.route("/")
    def home():
        return """
        <h1>Indahag Congregation Management System</h1>
        <hr>
        <h3>✅ Flask is running.</h3>
        <h3>✅ MySQL connection successful.</h3>
        """

    return app