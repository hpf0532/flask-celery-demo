import os 
import click

from flask import Flask, jsonify
from test_api.settings import config
from test_api.models import User

from celery import Celery

def make_celery(app):
    # 导入.env文件
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask('test_api')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    return app

def register_extensions(app):
    from test_api.extensions import db
    db.init_app(app)
#    celery_ext.init_app(app)

def register_blueprints(app):
    from test_api.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        response = jsonify(code=400, message="Bad Request")
        response.status_code = 400
        return response

    @app.errorhandler(403)
    def forbidden(e):
        response = jsonify(code=403, message="Forbidden")
        response.status_code = 403
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        response = jsonify(code=404, message="The requested URL was not found on the server.")
        response.status_code = 404
        return response

    @app.errorhandler(405)
    def method_not_allowed(e):
        response = jsonify(code=405, message='The method is not allowed for the requested URL.')
        response.status_code = 405
        return response

def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        print(repr(db))
        db.create_all()
        click.echo('Initialized database.')
