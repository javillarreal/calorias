import settings

class Config(object):
    DEBUG = settings.flask['DEBUG']
    CSRF_ENABLED = settings.flask['CSRF_ENABLED']
    SESSION_TYPE = settings.flask['SESSION_TYPE']
    SECRET_KEY = settings.flask['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = settings.flask['SQLALCHEMY_DATABASE_URI']
    JWT_SECRET_KEY = settings.flask['JWT_SECRET_KEY']
    IMAGE_UPLOADS = settings.flask['IMAGE_UPLOADS']
    ALLOWED_EXTENSIONS = settings.flask['ALLOWED_EXTENSIONS']
    IMAGE_TEMP = settings.flask['IMAGE_TEMP']
