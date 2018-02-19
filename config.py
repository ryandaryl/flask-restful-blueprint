# General

class Config(object):
    DEFAULT_ENVIRONMENT = 'Production'


# Environments

class Development(Config):
    DEBUG = True

class Testing(Config):
    pass

class Staging(Config):
    pass

class Production(Config):
    pass