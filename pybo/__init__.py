from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
migrate=Migrate()

def create_app():   # FLASK application factory
    # init FLASK application factory
    app = Flask(__name__)

    # config.py env
    app.config.from_object(config)

    # INIT ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # Blue Print
    from.views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app