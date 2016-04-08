#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,request, abort,jsonify
import uuid
from simple_redis_queue import SimpleRedisQueue


# ranjeet

app = Flask(__name__)
int_queue = SimpleRedisQueue('INT', 'ADD')

@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    job_id = str(uuid.uuid4())
    app.logger.info("created job-id %s" %job_id)
    tuple_val = (a, b, job_id)
    # put in redis queue
    int_queue.put(tuple_val)
    return jsonify(ready=False, result=job_id)


@app.route("/status/<job_id>")
def get_status(job_id):
    result_total = int_queue.get_redis().get(str(job_id))
    app.logger.debug("result %s for job-id : %s" %(result_total, job_id))
    if result_total is None:
        app.logger.warn("No result found for job-id : %s" %job_id)
        return jsonify(ready=False)
    return jsonify(ready=True, result=result_total)


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.logger.info("Run on host :  %s and port : %s" %(host, str(port)))
    app.run(host=host, port=port)
