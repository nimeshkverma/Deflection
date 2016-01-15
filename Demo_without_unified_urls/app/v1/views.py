from flask import Blueprint, jsonify, request

v1 = Blueprint('v1', __name__)

from utils import get_response


@v1.route('/dummy_post', methods=['POST'])
@v1.route('/dummy_get', methods=['GET'])
def dummy_view():
    response = get_response(request)
    return jsonify(response)
