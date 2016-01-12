from flask import Blueprint, jsonify, request

v1 = Blueprint('v1', __name__)

from mapping import URL
from utils import get_response


@v1.route('/version_one_post_one', methods=['POST'])
@v1.route('/version_one_get_one', methods=['GET'])
def dummy_view():
    response = get_response(request)
    return jsonify(response)
