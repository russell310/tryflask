import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, 'db.sqlite3')
DEBUG = os.getenv("DEBUG")


class Config(object):
    """
    Common configurations
    """
    DEBUG = DEBUG

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """
    Production configurations
    """


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
