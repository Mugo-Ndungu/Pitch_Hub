import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:aaronmichelle@localhost/pitches'
    SQLALCHEMY_TRACk_NOTIFICATIONS = False
    SECRET_KEY = 'os.environ.get("SECRET_KEY")'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'PITCH HUB'
    SENDER_EMAIL  = 'twinnymugo@gmail.com'

    pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
