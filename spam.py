
from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def example():
    return "The API Call Was Completed, Thank You For Using Yancy", 200


@app.route('/api', methods=['POST'])
def spam_detection():
    data = request.json
    return jsonify({'response': 200, 'results': data})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
