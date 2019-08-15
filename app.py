#!/usr/bin/env python
import os

from flask import Flask, jsonify

ENV_MODE = os.environ.get('ENV_MODE', '').lower()

app = Flask(__name__)

@app.route('/')
def index_get():
    # print('')
    data = {
        'status' : 'OK',
        'version' : 'master-0.0.4',
        'environment' : ENV_MODE
    }
    return jsonify(data)
