from flask import Blueprint
from flask_restful import Api
from app.views import Home, HealthCheck, SampleApi

BaseRoutes = Blueprint('base_routes', __name__, cli_group=None)
ApiRoutes = Blueprint('api_routes', __name__, cli_group=None)

api = Api(ApiRoutes)

BaseRoutes.add_url_rule('/', view_func=Home.as_view('home'))
BaseRoutes.add_url_rule('/health_check', view_func=HealthCheck.as_view('health_check'))
api.add_resource(SampleApi, '/sample-api')