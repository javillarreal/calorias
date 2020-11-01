from dotenv import load_dotenv
load_dotenv()

import os

flask = {
    'DEBUG': os.getenv('DEBUG'),
    'CSRF_ENABLED': os.getenv('CSRF_ENABLED'),
    'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL'),
    'SESSION_TYPE': os.getenv('SESSION_TYPE'),
    'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY')
}
