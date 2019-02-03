from flask import Flask, request, jsonify, Response
import json
from . import routes

@routes.route('/spam', methods=['POST'])
def spam_detection():
    data = request.json
    ## We should run the classification SVM here
    ## We will use scikit-learn to do the SVM
    return jsonify({'response': 200, 'results': data})
