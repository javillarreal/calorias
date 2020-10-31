import settings

class Config(object):
    DEBUG = settings.flask['DEBUG']
    CSRF_ENABLED = settings.flask['CSRF_ENABLED']
    SECRET_KEY = settings.flask['SECRET_KEY']
    SESSION_TYPE = settings.flask['SESSION_TYPE']
    SQLALCHEMY_DATABASE_URI = settings.flask['SQLALCHEMY_DATABASE_URI']
