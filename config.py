import settings

class Config(object):
    DEBUG = settings.flask['DEBUG']
    CSRF_ENABLED = settings.flask['CSRF_ENABLED']
    SESSION_TYPE = settings.flask['SESSION_TYPE']
    SQLALCHEMY_DATABASE_URI = settings.flask['SQLALCHEMY_DATABASE_URI']
    JWT_SECRET_KEY = settings.flask['JWT_SECRET_KEY']
