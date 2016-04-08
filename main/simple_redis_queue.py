import redis
import logging
import os
from logging.config import fileConfig
fileConfig(os.path.join(os.path.dirname(__file__) , 'logging_config.ini'))
# fileConfig('logging_config.ini')
logging = logging.getLogger("simple_redis_queue")

# ranjeet

class SimpleRedisQueue(object):
    """Simple Queue with Redis list"""
    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default redis connection : host='localhost', port=6379"""
        self.__db= redis.Redis(**redis_kwargs)
        self.key = '%s:%s' %(namespace, name)
        logging.info("Redis key : %s  param : %s"%(self.key,str(redis_kwargs)))
        logging.info("The default redis connection : host='localhost', port=6379")

    def get_redis(self):
        return self.__db

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        logging.debug("Addded for key : %s item in list : %s"%(self.key,str(item)))
        self.__db.rpush(self.key, item)

    def get(self):
        """Remove and return an item from the queue.
        """
        item = self.__db.lpop(self.key)

        # if item:
        #     item = item[1]
        #     logging.debug("Removed for key : %s item in list : %s"%(self.key,str(item)))
        return item

