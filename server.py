
from flask import Flask, request, jsonify, Response
import json
from routes import *
from db import *

app = Flask(__name__)
app.register_blueprint(routes)

db_connection()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
