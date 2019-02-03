
from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def example():
    return "api call complete"

@app.route('/api', methods=['POST'])
def spam_detection():
    data = request.json
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
