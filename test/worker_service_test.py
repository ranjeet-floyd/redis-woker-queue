import unittest
import logging
import sys
import uuid
from logging.config import fileConfig
import os
fileConfig('logging_config.ini')
logging = logging.getLogger("TestWorkerService")
scriptpath = "../main"
sys.path.insert(1, os.path.abspath(scriptpath))
import worker_service as ws
# ranjeet

class TestWorkerService(unittest.TestCase):

    """ Test cases for FileUtils class methods """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_queue_worker_redis(self):
        logging.info("*" * 80)
        # check for redis server
        redis = ws.int_queue.get_redis()
        ping = redis.ping()
        # assert the status of the response
        self.assertEqual(ping,True)

    def test_queue_worker(self):
        logging.info("*" * 80)
        job_id = str(uuid.uuid4())
        # put on redis
        a = 1
        b = 2
        value = (a,b,job_id)
        put = ws.int_queue.put(value)
        ws.queue_worker() # run queue_worker
        result_total = ws.int_queue.get_redis().get(str(job_id))
        logging.info("sum for a :%s, b : %s is  :  %s"%(a, b, result_total))
        # assert the sum
        self.assertNotEqual(result_total, '')


if __name__ == "__main__":
    unittest.main()
    logging.info("*" * 80)
