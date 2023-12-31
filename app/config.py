import os


class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")

    # Database configuration

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:martinez@"
        "localhost:5432/Datos_App"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration variables as needed


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:martinez@"
        "localhost:5432/Datos_App"
    )


class ProductionConfig(Config):
    DEBUG = False
    # Add other production configurations here


# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    # Add other environments if needed
}
