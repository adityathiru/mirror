import re
import os
from webapp.utils.config import SUPPORTED_CONFIGURATIONS
from elasticsearch import Elasticsearch


class ElasticWriter(object):
    """ Elasticindex wrapper class """

    def __init__(self, host='localhost', port=9200, e_index=None):
        self._index = e_index
        self.es = Elasticsearch([{'host': host, 'port': port}])

    def write(self, doc, doc_type='document'):
        """ Write document to Elastic """
        return self.es.index(index=self._index, doc_type=doc_type, body=doc)

    def create(self, new_index, request_body=None):
        """ Create a new index """
        if request_body is None:
            request_body = {
                "settings": {
                    "index": {
                        "number_of_shards": 2,
                        "number_of_replicas": 1
                    }
                }
            }

        return self.es.indices.create(index=new_index, body=request_body)


def get_backend(requirements_dict):
    if all([requirements_dict.get('cuda_version'), requirements_dict.get('cuda_version') in SUPPORTED_CONFIGURATIONS['SUPPORTED_GPU']]):
        return requirements_dict['cuda_version']
    else:
        return 'cpu'


def validate_form(form_dict):
    form_dict['project_name'] = form_dict['project_name'].lower()
    if not re.match("^[a-z0-9_]*$", form_dict['project_name']):
        return "Please use lowercase numbers and underscore for project_name."
    if not os.path.isabs(form_dict['project_path']):
        return "Please enter the absolute path for project path."
    else:
        return True


if __name__ == '__main__':
    print(validate_form({"project_name":"Project_123","project_path" : "/user/project_name"}))