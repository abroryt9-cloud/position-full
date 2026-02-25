import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'position-secret-key-2026')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///position.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    NOWPAYMENTS_API_KEY = os.environ.get('NOWPAYMENTS_API_KEY', '')
    NOWPAYMENTS_WALLET = os.environ.get('NOWPAYMENTS_WALLET', '')
    CROSSMINT_API_KEY = os.environ.get('CROSSMINT_API_KEY', '')
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
