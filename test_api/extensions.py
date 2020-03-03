from flask_sqlalchemy import SQLAlchemy
from flask_celeryext import FlaskCeleryExt

db = SQLAlchemy()
celery_ext = FlaskCeleryExt()
