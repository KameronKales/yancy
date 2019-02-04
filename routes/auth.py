from flask import Flask, request, jsonify, Response
import json
from . import routes
from pprint import pprint
import psycopg2
import psycopg2.extras as e
from flask import Response


@routes.route("/auth", methods=['GET'])
def handle_verification():
    connection = "host='yancy.c89ytzifs5b6.us-east-1.rds.amazonaws.com' dbname='kam' user='kam' password='Kales333' port='5432'"
    conn = psycopg2.connect(connection)
    cursor = conn.cursor(cursor_factory=e.RealDictCursor)
    api_key = request.args.get('api')
    sql = "SELECT email, website FROM users where uuid_ = '{0}'".format(api_key)
    cursor.execute(sql)
    if not cursor.rowcount:
        print "No results found"
        return jsonify({'response': 401, 'results': 'Unauthorized'})
    else:
        user_info = cursor.fetchall()
        print user_info
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'response': 200, 'results': user_info})
