from flask import Flask, request, jsonify, Response
import json
from routes import *


app = Flask(__name__)
app.register_blueprint(routes)


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'response': 200, 'results': 'Completed Test'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
