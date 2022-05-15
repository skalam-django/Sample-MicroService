from app.utils import CustomException

def sample_function(q:any, b:bool=False):
    # Any other operations
    if q is None:
        raise CustomException('missing params')
    try:
        int(q)
        raise CustomException('invalid input format')
    except CustomException as e:
        raise e
    except:
        pass
    return {'q' : q, 'b' : b}