import psycopg2
import psycopg2.extras as e
from flask import Flask, request, jsonify, Response
from redis import Redis
from rq import Queue, Worker, Connection

redis_url = ('redis://redis:6379/0')
q = Queue(connection=redis_url)

def db_insert(data_to_send):
    api_key = data_to_send['api_key']
    text = data_to_send['spam']
    spam_classification = data_to_send['spam_classification']
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    sql = "INSERT INTO spam_classifier(uuid, text, classification) VALUES('{0}', '{1}', '{2}')".format(api_key, text, spam_classification)
    print sql
    cursor.execute(sql)
    print 'Cursor was here', cursor.execute(sql)
    if not cursor.rowcount:
        conn.commit()
        cursor.close()
        conn.close()
        return
    else:
        conn.commit()
        cursor.close()
        conn.close()
        return
