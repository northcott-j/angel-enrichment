from os import environ


class BaseConfig(object):
    DEBUG = False
    FLASK_ENV = environ.get('FLASK_ENV', None)
    FLASK_DEV_NAME = environ.get('FLASK_DEV_NAME', 'James Bond')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 5001
    HOME_URI = 'http://localhost:5001/'


class ProductionConfig(BaseConfig):
    HOST = '0.0.0.0'
    # Probably set these in your .env
    PORT = environ.get('PORT', None)
    HOME_URI = environ.get('HOME_URI', None)
