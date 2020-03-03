import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    TODOISM_LOCALES = ['en_US', 'zh_Hans_CN']
    TODOISM_ITEM_PER_PAGE = 20

    BABEL_DEFAULT_LOCALE = TODOISM_LOCALES[0]

    # SERVER_NAME = 'todoism.dev:5000'  # enable subdomain support
    SECRET_KEY = os.getenv('SECRET_KEY', 'a secret string')
    #CELERY_TASK_EAGER_PROPAGATES=True
    #CELERY_TASK_ALWAYS_EAGER=True

    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data.db'))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://ansible:111111@127.0.0.1:3306/ansible?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CELERY_RESULT_BACKEND='redis://127.0.0.1:6379/4'
    CELERY_BROKER_URL='redis://127.0.0.1:6379/3'
    # CELERY_CACHE_BACKEND='memory'

class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

