from flask import Blueprint, jsonify

v3 = Blueprint('v3', __name__)


@v3.route('/dummy/', methods=['GET'])
def dummy_view():
    return jsonify(
        {
            "API_URL": "/3/dummy",
            "API_VERSION": 3
        }
    )
