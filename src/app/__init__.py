from flask import Flask, has_request_context, request
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
import logging
from app import settings



swagger_spec = APISpec(
    title = settings.PROJECT_NAME,
    version=f'v{int(float(settings.VERSION))}',
    plugins=[MarshmallowPlugin(),],
    openapi_version='2.0.0'
)


def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = settings.SECRET_KEY
    application.config['JSON_SORT_KEYS'] = False
    register_blueprints(application)
    if settings.ENABLE_LOGGING:
        configure_logging(application)
    configure_swagger(application)
    return application

def register_blueprints(application):
    from app.routes import BaseRoutes, ApiRoutes
    application.register_blueprint(BaseRoutes, url_prefix='', cli_group=None)
    application.register_blueprint(ApiRoutes, url_prefix=f'/api/v{int(float(settings.VERSION))}', cli_group=None)


def configure_swagger(application):
    from app.views import SampleApi
    application.config.update({
        'APISPEC_SPEC' : swagger_spec,
        'APISPEC_SWAGGER_URL' : '/swagger/',
        'APISPEC_SWAGGER_UI_URL' : '/swagger-ui/'
    })
    docs = FlaskApiSpec(application)
    docs.register(SampleApi, blueprint='api_routes', endpoint='')


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None                
        return super().format(record)


def configure_logging(application):
    from flask.logging import default_handler
    from logging.handlers import RotatingFileHandler

    formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )

    file_handler = RotatingFileHandler('flaskapp.log', maxBytes=16384, backupCount=1)
    file_handler.setFormatter(formatter)

    application.logger.removeHandler(default_handler)
    application.logger.addHandler(file_handler)


