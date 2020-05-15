class BaseConfig(object):
    """
    Base config class
    """

    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    """
    Production specific config
    """

    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """
    Development environment specific configuration
    """

    DEBUG = True
    TESTING = True
    API_KEY = "b089e5f0d374b1d1de404998536dbd09"
    API_SECRET = "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"