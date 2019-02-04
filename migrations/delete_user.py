import psycopg2
import psycopg2.extras as e
from flask import Response

email = 'edwardsdalton97@gmail.com'

def delete_user(email):
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    cursor.execute("delete from users where email ='{0}'".format(email))
    conn.commit()
    cursor.close()
    conn.close()
    return Response, 200

delete_user(email)
