import requests
import unittest
from webapp.utils.tools import get_backend,validate_form


class endpoints(unittest.TestCase):
    def test_endpoints(self):
        self.assertEqual(requests.get("http://0.0.0.0:8000/configurator").status_code, 200)

    def test_get_backend(self):
    	self.assertEqual(get_backend({'cuda_version':'cuda8'}),'cuda8')
    	self.assertEqual(get_backend({'cuda_version':'cuda9'}),'cuda9')
    	self.assertEqual(get_backend({'cuda_version':'cuda10'}),'cuda10')
    	self.assertEqual(get_backend({'cuda_version':'cuda'}),'cpu')
    	self.assertEqual(get_backend({'cuda_version':'cpu'}),'cpu')
    	self.assertEqual(get_backend({'cuda_version':''}),'cpu')

    def test_validate_form(self):
    	self.assertTrue(validate_form({"project_name":"mark_1","project_path":"/user/bharath"}))
    	self.assertEqual(validate_form({"project_name":"mark_1@#","project_path":"/user/bharath"}),"Please use lowercase numbers and underscore for project_name.")
    	self.assertEqual(validate_form({"project_name":"mark_1","project_path":"user/bharath"}),"Please enter the absolute path for project path.")
    	self.assertTrue(validate_form({"project_name":"Mark_123","project_path":"/user/bharath"}))
    	self.assertTrue(validate_form({"project_name":"Mark_123","project_path":"/"}))



if __name__ == '__main__':
    unittest.main()
