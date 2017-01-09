import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xab\xb8\x05\xb8\xd1\x19IT\xcd\x92\xef\x95g>\xbd\xbe\xff\xa5Z\xc4EwG\xf9'
    SQLALCHEMY_DATABASE_URI = os.environ.setdefault('DATABASE_URL', 'sqlite:///posts.db')
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopConfig(BaseConfig):
    DEBUG = True


class ProductConfig(BaseConfig):
    DEBUG = False
