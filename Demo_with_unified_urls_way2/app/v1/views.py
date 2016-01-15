from flask import Blueprint, jsonify, request

v1 = Blueprint('v1', __name__)

from utils import get_response


def dummy_view():
    response = get_response(request)
    return jsonify(response)


def dummy_view():
    response = get_response(request)
    return jsonify(response)
