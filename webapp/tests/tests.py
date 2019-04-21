import requests
import unittest 
  
class endpoints(unittest.TestCase):
    def test(self):
    	self.assertEqual(requests.get("http://0.0.0.0:8000/requirements").status_code,200)

if __name__ == '__main__':
    unittest.main()