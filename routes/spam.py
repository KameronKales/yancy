from flask import Flask, request, jsonify, Response
import json
import psycopg2
import psycopg2.extras as e
from . import routes
from brain_model import spam_svc_classifier
import time
from store_classification import db_insert
from rq.job import Job
from redis import Redis
import os
from rq import Queue

redis_url = ('redis://redis:6379/0')
q = Queue(connection=redis_url)

@routes.route('/v0/spam', methods=['POST'])
def spam():
    print request
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
                print api_key
                spam = request.json['spam']
                print spam
                spam_classification = spam_svc_classifier(spam)
                print spam_classification
                if spam_classification == 0:
                    spam_classification = 'False'
                else:
                    spam_classification = 'True'
                data_to_send = {'api_key': api_key, 'spam': spam, 'spam_classification': spam_classification}
                job = q.enqueue(db_insert(data_to_send), data_to_send)
                print(job.get_id())
            return jsonify({'response': 200, 'results': spam_classification})
