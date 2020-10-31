from dotenv import load_dotenv
load_dotenv()

import os

flask = {
    'DEBUG': os.getenv('DEBUG'),
    'CSRF_ENABLED': os.getenv('CSRF_ENABLED'),
    'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL'),
    'SESSION_TYPE': os.getenv('SESSION_TYPE'),
    'SECRET_KEY': os.getenv('SECRET_KEY')
}

spotify = {
    'SPOTIFY_CLIENT_ID': os.getenv('SPOTIFY_CLIENT_ID'),
    'SPOTIFY_CLIENT_SECRET': os.getenv('SPOTIFY_CLIENT_SECRET'),
    'SPOTIFY_REDIRECT_URI': os.getenv('SPOTIFY_REDIRECT_URI'),
    'ENCRYPTION_KEY': os.getenv('SPOTIFY_ENCRYPTION_KEY')
}

twitter = {
    'TWITTER_CLIENT_ID': os.getenv('TWITTER_CLIENT_ID'),
    'TWITTER_CLIENT_SECRET': os.getenv('TWITTER_CLIENT_SECRET'),
    'TWITTER_REDIRECT_URI': os.getenv('TWITTER_REDIRECT_URI'),
    'ENCRYPTION_KEY': os.getenv('TWITTER_ENCRYPTION_KEY')
}

domain_url = 'https://stopifybot.herokuapp.com'
