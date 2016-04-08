#!/usr/bin/python
# -*- coding: utf-8 -*-

from simple_redis_queue import SimpleRedisQueue
from ast import literal_eval
import time
import logging
from logging.config import fileConfig
import os
fileConfig('logging_config.ini')
logging = logging.getLogger("worker_service")

# ranjeet
int_queue = SimpleRedisQueue('INT', 'ADD')


def queue_worker():
    """
    Keep running
    :rtype: void | create jobid as key and total as value in redis
    """
    try:
        if int_queue.empty():
            logging.info("No job..redis queue is empty.")
            return
        tuple3 = int_queue.get()
        if tuple3:
            logging.debug ("received tuple3 :  %s" %str(tuple3))
            # convert tuple string to tuple object
            tup = tuple(literal_eval(tuple3,))
            if isinstance( tup[0], int ) and isinstance( tup[1] , int ):
                job_id = tup[2]
                logging.info('jobid : %s '%job_id)
                total = tup[0] + tup[1]
                # add job-id as key in redis
                int_queue.get_redis()[job_id]= total
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    logging.info ("start worker")
    # keep running
    while 1:
        logging.info("keep running ........")
        time.sleep(1)
        queue_worker()

