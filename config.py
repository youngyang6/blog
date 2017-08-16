import os

class Config:
    SECRET_KEY = 'hard to guess string' or os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'yangjian8618@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'y19860626'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <yangjian8618@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'yangjian8618@163.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/mysqldb'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/testdb'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/productdb'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
