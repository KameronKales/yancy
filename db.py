import psycopg2
import psycopg2.extras as e
from flask import Response

def connection():
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    #cursor.execute(sql)
    #rows = cursor.fetchall()
    #conn.commit()
    cursor.close()
    conn.close()
    print "Connection Run"
    return Response, 200

connection()
