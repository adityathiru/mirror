import yaml
from collections import OrderedDict 

def dockercompose_generate(data):
	with open('data.yml', 'w') as outfile:
	    yaml.dump(dict(data), outfile, default_flow_style=False)


if __name__ == '__main__':
	data = {
	      "webapp":{
	    "build":
	      {"context": "webapp/"},
	    "image": "projectmirror/webapp:1.0",
	    "volumes":[
	      "./webapp:/webapp",
	      "./webapp/data:/var/lib/data"],
	    "ports":
	      ["8000:8000"],
	    "networks":
	      ["elk"],
	    "restart": "on-failure"
	}
	dockercompose_generate(data)