import psycopg2
import psycopg2.extras as e
from flask import Response

email = 'edwardsdalton97@gmail.com'
website = 'www.console.chat'
add_new_user = 'INSERT INTO USERS(email, website) VALUES("{0}", "{1}")'.format(email, website)

print add_new_user

def add_new():
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    cursor.execute("INSERT INTO USERS(email, website) VALUES('insert_your_email', 'insert_your_website')")
    conn.commit()
    cursor.close()
    conn.close()
    return Response, 200


add_new()
