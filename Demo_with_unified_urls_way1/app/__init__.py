import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from config import VERSIONS_ALLOWED

from flask import Flask, jsonify, request
app = Flask(__name__)

from urls import URL_MAPPINGS


@app.route('/<version>/', defaults={'path': ''})
@app.route('/<version>/<path:path>')
def redirect(version, path):
    if URL_MAPPINGS.get(path):
        if URL_MAPPINGS[path].get(version) and version in VERSIONS_ALLOWED:
            return URL_MAPPINGS[path][version](request)
        else:
            return jsonify({'Response': 'Not A Supported Version'})
    else:
        return jsonify({'Response': 'Not A Supported API'})


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Message": "URL not supported"}), 404
