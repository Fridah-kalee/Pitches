import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kalee@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("testing@gmail.com")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oytwsfvqjadzgf:74e4dd3c6e4d7fd980643b681d9145baf3b98611eafcd639a33d8941229f67ab@ec2-3-217-113-25.compute-1.amazonaws.com:5432/d89nv1bn48c0fa'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://",1)
    uri = os.environ.get("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`
    SQLALCHEMY_DATABASE_URI = uri

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kalee@localhost/pitches_test'
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kalee@localhost/pitches'
    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}    