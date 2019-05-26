

class Config:
    DEBUG = True
    TESTTING = True
    SECRET_KEY = 'abcxyz'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:4801@localhost:3306/flaskdb?charset=utf8'







