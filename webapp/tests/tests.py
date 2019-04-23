import requests
import unittest
from webapp.utils.tools import get_backend,validate_form
from webapp.utils.executable_generator import ExecutableGenerator
from webapp.utils.installation import set_default_python, install_deeplearning_frameworks,install_editors


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

    def test_generate_function(self):
        self.assertEqual(ExecutableGenerator("/user/bharath",{"project_name":"mark_1","project_path":"/user/bharath"}).generate_function("function_name",["function_description"]),["function_name() {\n","function_description","\n}\n"])
        self.assertNotEqual(ExecutableGenerator("/user/bharath",{"project_name":"mark_1","project_path":"/user/bharath"}).generate_function("function_name",["function_description"]),["function_name() {\n","function_description","","\n}\n"])
        self.assertNotEqual(ExecutableGenerator("/user/bharath",{"project_name":"mark_1","project_path":"/user/bharath"}).generate_function("function_name",["function_description"]),["function_name() {\n","function_descript","","\n}\n"])
        self.assertNotEqual(ExecutableGenerator("/user/bharath",{"project_name":"mark_1","project_path":"/user/bharath"}).generate_function("function_name",["function_description"]),["function_name {\n","function_descript","","\n}\n"])
        self.assertNotEqual(ExecutableGenerator("/user/bharath",{"project_name":"mark_1","project_path":"/user/bharath"}).generate_function("function_name",["function_description"]),["function_name {\n","function_descript","","\n\n"])

    def test_set_default_python(self):
        self.assertEqual(set_default_python("python2"),['RUN rm -f /usr/bin/python2 && ln -s /usr/bin/python2.7 /usr/bin/python2', 'RUN rm -f /usr/bin/python && ln -s /usr/bin/python2.7 /usr/bin/python', 'RUN wget https://bootstrap.pypa.io/get-pip.py', 'RUN python2.7 get-pip.py', 'RUN rm get-pip.py'])
        self.assertEqual(set_default_python("python3"),['RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.6 /usr/bin/python3', 'RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.6 /usr/bin/python', 'RUN wget https://bootstrap.pypa.io/get-pip.py', 'RUN python3.6 get-pip.py', 'RUN rm get-pip.py'])

    def test_install_deeplearning_frameworks(self):
        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python2","cuda8"),['RUN pip install https://download.pytorch.org/whl/cu80/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl', 'RUN pip install torchvision', 'RUN pip install torchtext'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python2","cuda8"),['RUN pip install https://download.pytorch.org/whl/cu80/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl', 'RUN pip install torchvision', 'RUN pip install torchtext', 'RUN pip install tensorflow-gpu'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python3","cuda8"),['RUN pip3 install https://download.pytorch.org/whl/cu80/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python3","cuda8"),['RUN pip3 install https://download.pytorch.org/whl/cu80/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp', 'RUN pip3 install tensorflow'])

        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python2","cuda9"),['RUN pip install torch', 'RUN pip install torchvision', 'RUN pip install torchtext'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python2","cuda9"),['RUN pip install torch', 'RUN pip install torchvision', 'RUN pip install torchtext', 'RUN pip install tensorflow-gpu'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python3","cuda9"),['RUN pip3 install torch', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python3","cuda9"),['RUN pip3 install torch', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp', 'RUN pip3 install tensorflow-gpu'])

        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python2","cuda10"),['RUN pip install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl', 'RUN pip install torchvision', 'RUN pip install torchtext'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python2","cuda10"),['RUN pip install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp27-cp27mu-linux_x86_64.whl', 'RUN pip install torchvision', 'RUN pip install torchtext', 'RUN pip install tensorflow-gpu'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python3","cuda10"),['RUN pip3 install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python3","cuda10"),['RUN pip3 install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp', 'RUN pip3 install tensorflow-gpu'])

        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python2","cpu"),['RUN pip install torch', 'RUN pip install torchvision', 'RUN pip install torchtext'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python2","cpu"),['RUN pip install torch', 'RUN pip install torchvision', 'RUN pip install torchtext', 'RUN pip install tensorflow'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch"],"python3","cpu"),['RUN pip3 install torch', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp'])
        self.assertEqual(install_deeplearning_frameworks(["pytorch","tensorflow"],"python3","cpu"),['RUN pip3 install torch', 'RUN pip3 install torchvision', 'RUN pip3 install torchtext', 'RUN pip3 install allennlp', 'RUN pip3 install tensorflow'])

    def test_install_editors(self):
        self.assertEqual(install_editors(["vscode"],"python2"),['RUN cd / && wget https://github.com/codercom/code-server/releases/download/1.408-vsc1.32.0/code-server1.408-vsc1.32.0-linux-x64.tar.gz && tar -xzvf code-server1.408-vsc1.32.0-linux-x64.tar.gz && chmod +x code-server1.408-vsc1.32.0-linux-x64/code-server', 'COPY ./editors/docker-entrypoint.sh /usr/local/bin/', 'ENTRYPOINT ["docker-entrypoint.sh"]'])
        self.assertEqual(install_editors(["vscode"],"python3"),['RUN cd / && wget https://github.com/codercom/code-server/releases/download/1.408-vsc1.32.0/code-server1.408-vsc1.32.0-linux-x64.tar.gz && tar -xzvf code-server1.408-vsc1.32.0-linux-x64.tar.gz && chmod +x code-server1.408-vsc1.32.0-linux-x64/code-server', 'COPY ./editors/docker-entrypoint.sh /usr/local/bin/', 'ENTRYPOINT ["docker-entrypoint.sh"]'])

        self.assertEqual(install_editors(["vscode","jupyter"],"python2"),['RUN cd / && wget https://github.com/codercom/code-server/releases/download/1.408-vsc1.32.0/code-server1.408-vsc1.32.0-linux-x64.tar.gz && tar -xzvf code-server1.408-vsc1.32.0-linux-x64.tar.gz && chmod +x code-server1.408-vsc1.32.0-linux-x64/code-server', 'COPY ./editors/docker-entrypoint.sh /usr/local/bin/', 'ENTRYPOINT ["docker-entrypoint.sh"]', 'RUN pip install jupyter'])
        self.assertEqual(install_editors(["vscode","jupyter"],"python3"),['RUN cd / && wget https://github.com/codercom/code-server/releases/download/1.408-vsc1.32.0/code-server1.408-vsc1.32.0-linux-x64.tar.gz && tar -xzvf code-server1.408-vsc1.32.0-linux-x64.tar.gz && chmod +x code-server1.408-vsc1.32.0-linux-x64/code-server', 'COPY ./editors/docker-entrypoint.sh /usr/local/bin/', 'ENTRYPOINT ["docker-entrypoint.sh"]', 'RUN pip3 install jupyter'])

        self.assertEqual(install_editors(["jupyter"],"python2"),['RUN pip install jupyter'])
        self.assertEqual(install_editors(["jupyter"],"python3"),['RUN pip3 install jupyter'])


if __name__ == '__main__':
    unittest.main()
