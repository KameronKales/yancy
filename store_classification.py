import psycopg2
import psycopg2.extras as e
from flask import Flask, request, jsonify, Response
from redis import Redis
from rq import Queue, Worker, Connection

redis_url = ('redis://redis:6379/0')
q = Queue(connection=redis_url)

def db_insert(api_key, spam, spam_classification):
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    print conn
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    sql = "INSERT INTO spam_classifier(uuid, text, classification) VALUES('{0}', '{1}', '{2}')".format(api_key, spam, spam_classification)
    print sql
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return
