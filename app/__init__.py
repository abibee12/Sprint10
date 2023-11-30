from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)

    # Importar config_dict aquí para evitar la importación circular
    from app.config import config_dict
    app.config.from_object(config_dict[config_name])

    # Initialize the database
    db.init_app(app)

    # Importar blueprints/routes después de la inicialización de la aplicación
    from app.routes import data_routes

    # Initialize Flask-Migrate with the application and the database
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(data_routes)

    return app
