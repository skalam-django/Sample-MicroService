from marshmallow import Schema, fields

class String(fields.String):
    def _validate_missing(self, value):
        pass 


class SampleGetRequestSchema(Schema):
    q = String(required=True, description='String Param')
    b = fields.Bool(required=False, description='Boolean Param')

class GetDataSchema(Schema):
    q = String(default=None, description='null')
    b = fields.Bool(default=False, description='false')

class SampleGetResponseSchema(Schema):
    response_code = String(default='00', description='00')
    response_status = String(default='SUCCESS', description='SUCCESS')
    response_message = String(default='Success.', description='Success.')
    response_time = String(default=0.0, description='0.0')
    data = fields.Nested(GetDataSchema)


class SamplePostRequestSchema(Schema):
    q = String(required=True, description='String Param')
    b = fields.Bool(required=False, description='Boolean Param')

class PostDataSchema(Schema):
    q = String(default=None, description='null')
    b = fields.Bool(default=False, description='false')

class SamplePostResponseSchema(Schema):
    response_code = String(default='00', description='00')
    response_status = String(default='SUCCESS', description='SUCCESS')
    response_message = String(default='Success.', description='Success.')
    response_time = String(default=0.0, description='0.0')
    data = fields.Nested(PostDataSchema)


class SamplePutRequestSchema(Schema):
    q = String(required=True, description='String Param')
    b = fields.Bool(required=False, description='Boolean Param')

class PutDataSchema(Schema):
    q = String(default=None, description='null')
    b = fields.Bool(default=False, description='false')

class SamplePutResponseSchema(Schema):
    response_code = String(default='00', description='00')
    response_status = String(default='SUCCESS', description='SUCCESS')
    response_message = String(default='Success.', description='Success.')
    response_time = String(default=0.0, description='0.0')
    data = fields.Nested(PutDataSchema)

