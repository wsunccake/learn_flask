import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = os.environ.setdefault('DATABASE_URL', 'sqlite:///posts.db')
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopConfig(BaseConfig):
    DEBUG = True


class ProductConfig(BaseConfig):
    DEBUG = False
