import unittest
import logging
import  json
import sys
from logging.config import fileConfig
import os
fileConfig('logging_config.ini')
logging = logging.getLogger("worker_service")
scriptpath = "../main"
sys.path.insert(1, os.path.abspath(scriptpath))
import main_service as main_service
# ranjeet

# Test flask rest service
class TestMainService(unittest.TestCase):

    """ Test cases for FileUtils class methods """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = main_service.app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_add_numbers_status_code(self):
        logging.info("*" * 80)
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get("/add/10/11")
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_add_numbers_data(self):
        logging.info("*" * 80)
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get("/add/10/11")
        logging.info(result)
        # assert the response data
        self.assertNotEquals(result.data, None)


    def test_get_status_http_code(self):
        logging.info("*" * 80)
        result = self.app.get("/status/598303d2-ba84-4cef-a1b2-1fa25efe6ed3")
        self.assertEqual(result.status_code, 200)

    def test_get_status_http_code(self):
        logging.info("*" * 80)
        result = self.app.get("/status/598303d2-ba84-4cef-a1b2-1fa25efe6ed33")

        # assert the response data
        self.assertNotEqual(result.data, None)
        # assert the response json
        result_json = json.loads(result.data)
        if(result_json['ready'] == True):
            # assert the response json | never be empty
            self.assertNotEqual(result_json['result'], "")

if __name__ == "__main__":
    unittest.main()
    logging.info("*" * 80)
