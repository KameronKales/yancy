from flask import Flask, request, jsonify, Response
import json
import psycopg2
import psycopg2.extras as e
from . import routes
from nb import *

@routes.route('/spam', methods=['POST'])
def spam():
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    print request.json
    if 'api_key' not in request.json:
        return jsonify({'response': 401, 'results': 'Please add your api_key. If you are unsure how please contact support'})
    else:
        if 'spam' not in request.json:
            return jsonify({'response': 401, 'results': 'Please add your spam to be classified. If you are unsure how please contact support'})
        else:
            api_key = request.json['api_key']
            spam = request.json['spam']
            spam_classification = classifier(spam)
            if spam_classification == 0:
                spam_classification = 'False'
            else:
                spam_classification = 'True'
            sql = "INSERT INTO spam(uuid, content, classification) VALUES('{0}', '{1}', '{2}')".format(api_key, spam, spam_classification)
            ##cursor.execute(sql)
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
