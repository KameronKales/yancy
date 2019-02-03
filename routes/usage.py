from flask import Flask, request, jsonify, Response
import json
from . import routes

@routes.route('/usage', methods=['GET'])
def usage():
    user = request.args.get('user')
    ## Go to db and figure out how many requests user has made
    ## in last 30 days. If over plan limit, return 401.
    return "You are logged in as `{0}`".format(user), 200
