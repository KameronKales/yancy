from flask import Flask, request, jsonify, Response
import json
import psycopg2
import psycopg2.extras as e
from . import routes

@routes.route('/usage', methods=['GET'])
def usage():
    api_key = request.args.get('api_key')
    print api_key
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    sql = "SELECT COUNT(*) FROM spam where uuid = '{0}'".format(api_key)
    cursor.execute(sql)
    if not cursor.rowcount:
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'response': 401, 'results': 'Unauthorized'})
    else:
        user_info = cursor.fetchall()
        print user_info
        conn.commit()
        cursor.close()
        conn.close()
        if len(user_info) <= 50:
            return jsonify({'response': 200, 'results': user_info})
        else:
            return jsonify({'response': 401, 'results': 'Too many requests. Upgrade Your Plan'})
