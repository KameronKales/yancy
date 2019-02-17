from flask_script import Manager
from flask import Flask, request, jsonify, Response
import os
import redis
from rq import Worker, Queue, Connection
import click
from server import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

@app.cli.command('run_worker')
def run_worker():
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
