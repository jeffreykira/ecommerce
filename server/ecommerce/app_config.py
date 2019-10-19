
CONFIG = None


class Config:

    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 5604


class ProductionConfig(Config):
    DEBUG = False
    TEST = False
    PROD = True


class DevelopmentConfig(Config):
    DEBUG = True
    TEST = False
    PROD = False
    SWAGGER_UI_DOC_EXPANSION = 'list'


class UnitTestConfig(Config):
    DEBUG = False
    TEST = True
    PROD = False
    SERVER_PORT = 12345
