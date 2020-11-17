from dotenv import load_dotenv
load_dotenv()

import os

flask = {
    'DEBUG': os.getenv('DEBUG'),
    'CSRF_ENABLED': os.getenv('CSRF_ENABLED'),
    'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL'),
    'SESSION_TYPE': os.getenv('SESSION_TYPE'),
    'SECRET_KEY': os.getenv('SECRET_KEY'),
    'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY'),
    'IMAGE_UPLOADS': os.getenv('IMAGE_UPLOADS'),
    'IMAGE_TEMP': os.getenv('IMAGE_TEMP'),
    'ALLOWED_EXTENSIONS': os.getenv('ALLOWED_EXTENSIONS')
}
