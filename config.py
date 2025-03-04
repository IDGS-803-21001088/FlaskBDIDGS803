import os
from sqlalchemy import create_engine

import urllib

class Config(object):
    SECRET_KEY='Clave nueva'
    SESION_COOKIES_SECURE=False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cclab@127.0.0.1/bdidgs803'
    SQLALCHEMY_TACK_MODIFICATIONS=False
    
    