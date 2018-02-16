import os

class Config(object):
    DEFAULT_ENVIRONMENT = 'Production,Public'


# Environment attributes

class Local(Config):
    HOST = 'localhost'
    PORT = 80

class Public(Config):
    HOST = '0.0.0.0'
    PORT = os.environ.get('PORT') or 5000


# Environments

class Development(Local):
    DEBUG = True

class Testing(Config):
    pass

class Production(Config):
    pass


# Vendors

class Travis(Testing):
    PORT = 8000

class Heroku(Config):
    PORT = Public.PORT