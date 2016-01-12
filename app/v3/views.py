from flask import Blueprint, jsonify

v3 = Blueprint('v3', __name__)


@v3.route('/dummy_get', methods=['GET'])
def dummy_get_view():
    return jsonify(
        {
            "API_URL": "/3/dummy",
            "API_VERSION": 3,
            "API_METHOD": "GET",
        }
    )


@v3.route('/dummy_post', methods=['POST'])
def dummy_post_view():
    return jsonify(
        {
            "API_URL": "/3/dummy",
            "API_VERSION": 3,
            "API_METHOD": "POST",
        }
    )
