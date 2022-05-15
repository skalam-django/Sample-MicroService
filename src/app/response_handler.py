from flask import current_app, jsonify
import json 
from collections import OrderedDict
from app.models import Response
import traceback

def CustomResponse(message:str="success", data:any=None, response_time:float=0.0):
    try:
        obj = Response.query.filter_by(message)
        if obj is not None:
            res_data = OrderedDict()
            res_data["response_code"] = obj.response_code
            res_data["response_status"] = obj.response_status
            res_data["response_message"] = obj.response_message.title()
            res_data["response_time"] = response_time
            if message in ["sys error", ]:
                data = None 
            res_data["data"] = data    
            response_data = json.dumps(res_data, indent=4)
            placeholder = '_'*(len(response_data)-2)
            response = jsonify(placeholder)
            response.response[0] = response_data + '\n'
            return response
        else:
            return CustomResponse('sys error', None, response_time=response_time)    
    except Exception as e:
        current_app.logger.error(f"{traceback.format_exc()} \n{e}\n")