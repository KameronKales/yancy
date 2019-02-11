from flask import Flask, request, jsonify, Response
from . import routes
from rq import Queue
from rq.job import Job
from redis import Redis
redis_conn = Redis('localhost', 6379)
q = Queue(connection=redis_conn)

@routes.route('/test', methods=['GET'])
def test():
    return jsonify({'response': 200, 'results': 'Completed Test'})


@routes.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):
    job = Job.fetch(job_key, connection=redis_conn)
    if job.is_finished:
        return jsonify({'response': 200, 'job': job.result})
    else:
        return jsonify({'response': 202, 'job': job.result})
