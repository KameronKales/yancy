import psycopg2
import psycopg2.extras as e
from flask import Flask, request, jsonify, Response

def db_insert(api_key, text, spam_classification):
    print 'This is the api_key', api_key
    print 'This was the text', text
    print 'This was the spam_classification', spam_classification
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    sql = "INSERT INTO spam_classifier(uuid, text, classification) VALUES('{0}', '{1}', '{2}')".format(api_key, text, spam_classification)
    cursor.execute(sql)
    if not cursor.rowcount:
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'response': 401})
    else:
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'response': 200})
