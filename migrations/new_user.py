import psycopg2
import psycopg2.extras as e
from flask import Response

email = 'kameron.kales@gmail.com'
website = 'www.glance.ai'

def add_new(email, website):
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    cursor.execute("INSERT INTO USERS(email, website) VALUES('{0}', '{1}')".format(email, website))
    conn.commit()
    cursor.close()
    conn.close()
    return Response, 200

add_new(email, website)
