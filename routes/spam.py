from flask import Flask, request, jsonify, Response
import json
import psycopg2
import psycopg2.extras as e
from . import routes
from brain_model import spam_svc_classifier
import time
from store_classification import db_insert
from rq import Queue
from rq.job import Job
from worker import conn

q = Queue(connection=conn)
print q.jobs
#host=("'yancy-job-queue.xcgj4d.0001.use1.cache.amazonaws.com', db=0'")


@routes.route('/v0/spam', methods=['POST'])
def spam():
    #print request
    if not request.json:
        return jsonify({'response': 401, 'results': 'Please send your request with JSON formatted data'})
    else:
        if 'api_key' not in request.json:
            return jsonify({'response': 401, 'results': 'Please add your api_key. If you are unsure how please contact support'})
        else:
            if 'spam' not in request.json:
                return jsonify({'response': 401, 'results': 'Please add your spam to be classified. If you are unsure how please contact support'})
            else:
                api_key = request.json['api_key']
                spam = request.json['spam']
                spam_classification = spam_svc_classifier(spam)
                if spam_classification == 0:
                    spam_classification = 'False'
                else:
                    spam_classification = 'True'
                #print spam_classification
                ## we should run a redis queue to speed up the api result
                ## inserting into the db is slow, 15 seconds vs <1 without
                ## to make this more pleasant we will execute the insertion in the background
                job = q.enqueue_call(
                func=db_insert, args=(api_key, spam, spam_classification,), result_ttl=5000
                )
                print(job.get_id())
                #print job
                return jsonify({'response': 200, 'results': spam_classification})
