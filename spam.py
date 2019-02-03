
from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def example():
    return "The API Call Was Completed, Thank You For Using Yancy", 200

@app.route('/auth', methods=['POST'])
def auth_user():
    data = request.body
    print data
    return "Your Authorization Was Completed, You're now logged in", 200

@app.route('/usage', methods=['GET'])
def usage():
    ## not sure what the QS will be valid here
    ## we need this to log how many requests someone has made <= 30 days
    ## there probably is a library to do this 30 day calculation
    ## 30 days X 24 hours x 60 minutes x 60 seconds = total seconds
    ##
    data = request
    data
    return "You have used `{}`", data



@app.route('/spam', methods=['POST'])
def spam_detection():
    data = request.json
    ## We should run the classification SVM here
    ## We will use scikit-learn to do the SVM
    return jsonify({'response': 200, 'results': data})




if __name__ == "__main__":
    app.run(debug=True, port=5000)