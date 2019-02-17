from flask import Flask, request, jsonify, Response
import json
from routes import *
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://e46acac9ea124ad28f33b0087f803a1b@sentry.io/1396061",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'response': 200, 'results': 'Completed Test'})



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
