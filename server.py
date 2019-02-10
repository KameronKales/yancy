from flask import Flask, request, jsonify, Response
import json
from routes import *
from brain_model import *
from rq import Queue
from rq.job import Job
from worker import conn
from store_classification import db_insert
import rq_dashboard

q = Queue(connection=conn)
print q


app = Flask(__name__)
app.register_blueprint(routes)
app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/brain/rq")
##db = SQLAlchemy(app) <== update for our DB


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'response': 200, 'results': 'Completed Test'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
