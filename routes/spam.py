from flask import Flask, request, jsonify, Response
import json
import psycopg2
import psycopg2.extras as e
from . import routes
from brain_model import *
import os


@routes.route('/v0/spam', methods=['POST'])
def spam():
    if not request.json:
        return jsonify({'response': 401, 'results': 'Please send your request with JSON formatted data'})
    else:
        if 'api_key' not in request.json:
            return jsonify({'response': 401, 'results': 'Please add your api_key. If you are unsure how please contact support'})
        else:
            if 'spam' not in request.json:
                return jsonify({'response': 401, 'results': 'Please add your spam to be classified. If you are unsure how please contact support'})
            else:
                host = os.environ['HOST']
                dbname = os.environ['DBNAME']
                user = os.environ['USER']
                password = os.environ['PASSWORD']
                port = os.environ['PORT']
                connection = 'host={} dbname={} user={} password={} port={}'.format(
                    host, dbname, user, password, port)
                conn = psycopg2.connect(connection)
                cursor = conn.cursor(cursor_factory=e.RealDictCursor)
                api_key = request.json['api_key']
                spam = request.json['spam']
                spam_classification = spam_svc_classifier(spam)
                if spam_classification == 0:
                    spam_classification = 'False'
                else:
                    spam_classification = 'True'
                sql = "INSERT INTO spam_classifier(uuid, text, classification) VALUES('{0}', '{1}', '{2}')".format(
                    api_key, spam, spam_classification)
                cursor.execute(sql)
                if not cursor.rowcount:
                    conn.commit()
                    cursor.close()
                    conn.close()
                    return jsonify({'response': 401, 'results': 'Unauthorized'})
                else:
                    conn.commit()
                    cursor.close()
                    conn.close()
                    return jsonify({'response': 200, 'results': spam_classification})
