import unittest
import sys
from ast import literal_eval
import logging
import  json
# import flaskr
from logging.config import fileConfig
import os
print (os.path.join(os.path.dirname(__file__) , 'logging_config.ini'))
fileConfig(os.path.join(os.path.dirname(__file__) , 'logging_config.ini'))
logging = logging.getLogger("TestSimpleRedisQueue")
import main.simple_redis_queue as srq
# ranjeet

class TestSimpleRedisQueue(unittest.TestCase):

    """ Test cases for FileUtils class methods """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.redis_queue = srq.SimpleRedisQueue('TEST', 'TEST_ADD')

    def tearDown(self):
        pass

    def test_get_redis(self):
        logging.info("*" * 80)
        # check for redis server
        redis = self.redis_queue.get_redis()
        ping = redis.ping()
        # assert the status of the response
        self.assertEqual(ping,True)

    def test_put(self):
        logging.info("*" * 80)
        # put on redis
        value = "TEST_REDIS"
        put = self.redis_queue.put(value)
        result = self.redis_queue.get()
        logging.info(result)
        # assert the value
        self.assertEqual(result, value)


if __name__ == "__main__":
    unittest.main()
    logging.info("*" * 80)
