from flask import Flask, request, jsonify, Response
import json
from routes import *

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'response': 200, 'results': 'Unauthorized'})



if __name__ == "__main__":
    app.run(debug=True, port=5000)
