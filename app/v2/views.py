from flask import Blueprint, jsonify, request

v2 = Blueprint('v2', __name__)

from utils import get_response


@v2.route('/dummy_post', methods=['POST'])
@v2.route('/dummy_get', methods=['GET'])
def dummy_view():
    response = get_response(request)
    return jsonify(response)
