import unittest
from app import create_app, settings


class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        application = create_app()
        application.app_context().push()
        self.app = application.test_client()
        # other setup operations if any
        print("Application setup done")
        return super().setUp()
        
    def tearDown(self) -> None:
        # teardown operations if any
        print("Application teardown done")
        return super().tearDown()

    
class SampleApiTest(BaseCase):
    def test_all_cases(self) -> None:
        print(f"Testing {settings.PROJECT_NAME} {settings.VERSION}")
        base_url = f'/api/v{int(float(settings.VERSION))}/sample-api'
        headers = {"Content-Type" : "application/json"}
        print("Testing GET Method 1")
        q = 'Hello'
        b = True 
        url = f'{base_url}?q={q}&b={b}'
        response = self.app.get(url, headers=headers)
        print(f"Invoked url: {url}")
        self.assertEqual('00', response.json['response_code'])
        print("Comparison passed (00, response_code)")
        self.assertEqual('SUCCESS', response.json['response_status'])
        print("Comparison passed (SUCCESS, response_status)")
        self.assertEqual('Success.', response.json['response_message'])
        print("Comparison passed (Success., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(dict, type(data))
        print("Comparison passed (dictionary, datatype of data)")         
        self.assertEqual(q, data.get('q'))
        print(f"Comparison passed ({q}, q)")
        self.assertEqual(b, data.get('b'))
        print(f"Comparison passed ({b}, b)")
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")                


        print("Testing GET Method 2")
        q = 1
        b = True 
        url = f'{base_url}?q={q}&b={b}'
        response = self.app.get(url, headers=headers)
        print(f"Invoked url: {url}")
        self.assertEqual('11', response.json['response_code'])
        print("Comparison passed (11, response_code)")
        self.assertEqual('FAIL', response.json['response_status'])
        print("Comparison passed (FAIL, response_status)")
        self.assertEqual('Invalid Input Parameters.', response.json['response_message'])
        print("Comparison passed (Invalid Input Parameters., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(None, data)
        print("Comparison passed (None, data)")         
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")    


        print("Testing GET Method 3")
        url = f'{base_url}'
        response = self.app.get(url, headers=headers)
        print(f"Invoked url: {url}")
        self.assertEqual('10', response.json['response_code'])
        print("Comparison passed (10, response_code)")
        self.assertEqual('FAIL', response.json['response_status'])
        print("Comparison passed (FAIL, response_status)")
        self.assertEqual('Missing Parameters.', response.json['response_message'])
        print("Comparison passed (Missing Parameters., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(None, data)
        print("Comparison passed (None, data)")         
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")   



        print("Testing POST Method 1")
        q = 'Hello'
        b = True 
        url = f'{base_url}'
        data = {'q': q, 'b': b}
        response = self.app.post(url, json={'q' : q, 'b' : b}, headers=headers)
        print(f"Invoked url: {url}", "Data: ", data)
        self.assertEqual('00', response.json['response_code'])
        print("Comparison passed (00, response_code)")
        self.assertEqual('SUCCESS', response.json['response_status'])
        print("Comparison passed (SUCCESS, response_status)")
        self.assertEqual('Success.', response.json['response_message'])
        print("Comparison passed (Success., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(dict, type(data))
        print("Comparison passed (dictionary, datatype of data)")         
        self.assertEqual(q, data.get('q'))
        print(f"Comparison passed ({q}, q)")
        self.assertEqual(b, data.get('b'))
        print(f"Comparison passed ({b}, b)")
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")  


        print("Testing POST Method 2")
        q = '1'
        b = True 
        url = f'{base_url}'
        data = {'q': q, 'b': b}
        response = self.app.post(url, json=data, headers=headers)
        print(f"Invoked url: {url}", 'Data: ', data)
        self.assertEqual('11', response.json['response_code'])
        print("Comparison passed (11, response_code)")
        self.assertEqual('FAIL', response.json['response_status'])
        print("Comparison passed (FAIL, response_status)")
        self.assertEqual('Invalid Input Parameters.', response.json['response_message'])
        print("Comparison passed (Invalid Input Parameters., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(None, data)
        print("Comparison passed (None, data)")     
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")    


        print("Testing POST Method 3")
        url = f'{base_url}'
        data = {}
        response = self.app.post(url, json=data, headers=headers)
        print(f"Invoked url: {url}", "Data: ", data)
        self.assertEqual('10', response.json['response_code'])
        print("Comparison passed (10, response_code)")
        self.assertEqual('FAIL', response.json['response_status'])
        print("Comparison passed (FAIL, response_status)")
        self.assertEqual('Missing Parameters.', response.json['response_message'])
        print("Comparison passed (Missing Parameters., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(None, data)
        print("Comparison passed (None, data)")        
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")   



        print("Testing PUT Method 1")
        q = 'Hello'
        b = True 
        url = f'{base_url}'
        data = {'q': q, 'b': b}
        response = self.app.put(url, json=data, headers=headers)
        print(f"Invoked url: {url}", "Data: ", data)
        self.assertEqual('00', response.json['response_code'])
        print("Comparison passed (00, response_code)")
        self.assertEqual('SUCCESS', response.json['response_status'])
        print("Comparison passed (SUCCESS, response_status)")
        self.assertEqual('Success.', response.json['response_message'])
        print("Comparison passed (Success., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(dict, type(data))
        print("Comparison passed (dictionary, datatype of data)")         
        self.assertEqual(q, data.get('q'))
        print(f"Comparison passed ({q}, q)")
        self.assertEqual(b, data.get('b'))
        print(f"Comparison passed ({b}, b)")
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")  


        print("Testing PUT Method 2")
        q = '1'
        b = True 
        url = f'{base_url}'
        data = {'q': q, 'b': b}
        response = self.app.put(url, json=data, headers=headers)
        print(f"Invoked url: {url}", "Data: ",data)
        self.assertEqual('11', response.json['response_code'])
        print("Comparison passed (11, response_code)")
        self.assertEqual('FAIL', response.json['response_status'])
        print("Comparison passed (FAIL, response_status)")
        self.assertEqual('Invalid Input Parameters.', response.json['response_message'])
        print("Comparison passed (Invalid Input Parameters., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(None, data)
        print("Comparison passed (None, data)")    
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")    


        print("Testing PUT Method 3")
        url = f'{base_url}'
        data = {}
        response = self.app.put(url, json=data, headers=headers)
        print(f"Invoked url: {url}", "Data: ", data)
        self.assertEqual('10', response.json['response_code'])
        print("Comparison passed (10, response_code)")
        self.assertEqual('FAIL', response.json['response_status'])
        print("Comparison passed (FAIL, response_status)")
        self.assertEqual('Missing Parameters.', response.json['response_message'])
        print("Comparison passed (Missing Parameters., response_message)")
        self.assertEqual(True, response.json['response_time']>0)
        print("Comparison passed (YES, response_time>0)")
        data = response.json.get('data')
        self.assertEqual(None, data)
        print("Comparison passed (None, data)")         
        self.assertEqual(200, response.status_code)
        print(f"Comparison passed (200, status_code)")   
