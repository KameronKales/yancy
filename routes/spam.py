from flask import Flask, request, jsonify, Response
import json
import psycopg2
import psycopg2.extras as e
from . import routes

@routes.route('/spam', methods=['POST'])
def spam():
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    api_key = request.json['api_key']
    spam = request.json['spam']
    classification = True
    print spam
    ## insert spam into spam table with uuid = api_key
    ## spam table has 3 columns. uuid, content, classification
    ## uuid = api_key (varchar 12 character limit)
    ## content = the actual spam we want to classify (varchar 500,000 character limit)
    ## classification = the classifier we ran (boolean)
    sql = "INSERT INTO spam(uuid, content, classification) VALUES('{0}', '{1}', '{2}')".format(api_key, spam, classification)
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
        return jsonify({'response': 200})
