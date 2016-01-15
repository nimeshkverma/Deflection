from flask import Blueprint, jsonify, request

v2 = Blueprint('v2', __name__)

from utils import get_response


def dummy_view():
    response = get_response(request)
    return jsonify(response)
