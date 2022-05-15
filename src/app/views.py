import time
import traceback
from flask import request, current_app, redirect
from flask_restful import Resource
from flask.views import MethodView
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from app.schema import (
                            Schema, 
                            SampleGetRequestSchema, 
                            SampleGetResponseSchema, 
                            SamplePostRequestSchema, 
                            SamplePostResponseSchema,
                            SamplePutRequestSchema,
                            SamplePutResponseSchema
)
from app.response_handler import CustomResponse
from app.utils import CustomException, truthy, falsy
from modules.module import sample_function


class Home(MethodView):
    def get(self):
        return redirect('/swagger-ui/')

class HealthCheck(MethodView):
    def get(self):
        return f"<STRONG>Sample Microservice</STRONG> is <STRONG style='color: #2a8552'>RUNNING</STRONG><br><span>Timestamp: {time.strftime('%D %H:%M:%S')}</span>"


class SampleApi(MethodResource, Resource):
    @doc(description='Sample Api', tags=['Test GET method'])
    @use_kwargs(SampleGetRequestSchema, location=('query'))
    @marshal_with(SampleGetResponseSchema, code=200, description='OK')
    @marshal_with(Schema, code=500, description='Something went wrong')
    def get(self, *args, **kwargs):
        message = 'sys error'
        data = None
        start_time = time.time()
        try:
            q = request.args.get('q')
            b = request.args.get('b')
            b = b in truthy
            data = sample_function(q, b)
            message = 'success'
        except CustomException as e:
            current_app.logger.warning(f"{traceback.format_exc()} \n{e}\n")
            message = str(e)
        except Exception as e:
            current_app.logger.error(f"{traceback.format_exc()} \n{e}\n")
            message = 'sys error'

        end_time = time.time()
        response = CustomResponse(
            message = message,
            data = data,
            response_time = end_time - start_time
        )
        current_app.logger.debug(f"message: {message}")
        return response

    @doc(description='Sample Api', tags=['Test POST method'])
    @use_kwargs(SamplePostRequestSchema, location=('json'))
    @marshal_with(SamplePostResponseSchema, code=200, description='OK')
    @marshal_with(Schema, code=500, description='Something went wrong')
    def post(self, *args, **kwargs):
        message = 'sys error'
        data = None
        start_time = time.time()
        try:
            q = request.json.get('q')
            b = request.json.get('b')
            b = b in truthy
            data = sample_function(q, b)
            message = 'success'
        except CustomException as e:
            current_app.logger.warning(f"{traceback.format_exc()} \n{e}\n")
            message = str(e)
        except Exception as e:
            current_app.logger.error(f"{traceback.format_exc()} \n{e}\n")
            message = 'sys error'
            
        end_time = time.time()
        response = CustomResponse(
            message = message,
            data = data,
            response_time = end_time - start_time
        )
        current_app.logger.debug(f"message: {message}")
        return response


    @doc(description='Sample Api', tags=['Test PUT method'])
    @use_kwargs(SamplePutRequestSchema, location=('json'))
    @marshal_with(SamplePutResponseSchema, code=200, description='OK')
    @marshal_with(Schema, code=500, description='Something went wrong')
    def put(self, *args, **kwargs):
        message = 'sys error'
        data = None
        start_time = time.time()
        try:
            q = request.json.get('q')
            b = request.json.get('b')
            b = b in truthy
            data = sample_function(q, b)
            message = 'success'
        except CustomException as e:
            current_app.logger.warning(f"{traceback.format_exc()} \n{e}\n")
            message = str(e)
        except Exception as e:
            current_app.logger.error(f"{traceback.format_exc()} \n{e}\n")
            message = 'sys error'

        end_time = time.time()
        response = CustomResponse(
            message = message,
            data = data,
            response_time = end_time - start_time
        )
        current_app.logger.debug(f"message: {message}")
        return response