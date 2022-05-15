import json
from app import settings

class Query(object):
    response_code = None
    response_status = None 
    response_message = None 
    internal_message = None 
    with open(settings.CONFIG_DIR / 'response.json', 'r', encoding='utf-8') as f:
        response_data = json.loads(f.read())
    def filter_by(self, internal_message:any=None):
        data = self.response_data.get(internal_message)
        if data is not None:
            self.response_code = data.get('response_code')
            self.response_status = data.get('response_status')
            self.response_message = data.get('response_message')
            return self
        return None 


class Response(object):
    query = Query()    