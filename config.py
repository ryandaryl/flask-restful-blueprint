import os

class Config(object):
    DEFAULT_ENVIRONMENT = 'Production'


# Environments

class Development(Config):
    DEBUG = True

class Testing(Config):
    pass

class Production(Config):
    pass