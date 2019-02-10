from flask import Flask, request, jsonify, Response
from . import routes
from rq import Queue
from rq.job import Job
from worker import conn

q = Queue(connection=conn)

@routes.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):
    job = Job.fetch(job_key, connection=conn)
    if job.is_finished:
        return jsonify({'response': 200, 'job': job.result})
    else:
        return jsonify({'response': 202, 'job': job.result})
