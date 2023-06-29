class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://flask:flask@db:3306/flask"
    SECRET_KEY = "sadasdsdssadsadsadsadsadssaddas"


class DevelopmentConfig(Config):
    DEBUG = True
