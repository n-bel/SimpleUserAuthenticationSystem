import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLACHEMY_DATABASE_URI = 'sqllite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False