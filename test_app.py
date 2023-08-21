import unittest
from app import app
import json

class TestFanApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fan App', response.data)

    def test_get_init(self):
        response = self.client.get('/api/fan/init')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('speed', data)
        self.assertIn('direction', data)

    def test_speed_up(self):
        for i in range(4):
            response = self.client.get('/api/fan/speedup', headers = {'speed' : i} )
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertTrue( data == ((i + 1) % 4))

    def test_normal_reverse(self):
        response = self.client.get('/api/fan/reverse', headers = {'dir' : 'normal'})
        data = response.data.decode()
        self.assertEqual(response.status_code, 200)    
        self.assertEqual(data, 'reverse')
        
    def test_reverse_normal(self):
        response = self.client.get('/api/fan/reverse', headers = {'dir' : 'reverse'})
        data = response.data.decode()
        self.assertEqual(response.status_code, 200)    
        self.assertEqual(data, 'normal')


    def test_invalid_speed_update(self):
        initial_speed = [-1, float('-inf'), -1.5 , 4, float('inf'), 100.4, 'sr', None, False]
        for i in initial_speed:
            response = self.client.get('/api/fan/speedup', headers = {'speed' : i} )
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertTrue( data == 0)

    def test_invalid_speed_request(self):
        response = self.client.get('/api/fan/speedup' )
        self.assertEqual(response.status_code, 400)


    def test_invalid_direction_update(self):
        initial_dir = [-1, float('-inf'), -1.5 , 4, float('inf'), 100.4, 'sr', None, False]
        for i in initial_dir:
            response = self.client.get('/api/fan/reverse', headers = {'dir' : i})
            data = response.data.decode()
            self.assertEqual(response.status_code, 200)    
            self.assertEqual(data, 'normal')
            
    def test_invalid_direction_request(self):
        response = self.client.get('/api/fan/reverse' )
        self.assertEqual(response.status_code, 400)


    def test_error_page_not_found(self):
        response = self.client.get('/api/fan/wrongpage')
        self.assertEqual(response.status_code, 404)

    def test_error_server(self):
        response = self.client.get('/api/fan/checkservererror')
        self.assertEqual(response.status_code, 500)
        

if __name__ == '__main__':
    unittest.main()