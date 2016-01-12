from flask import Blueprint, jsonify

v2 = Blueprint('v2', __name__)


@v2.route('/dummy/', methods=['GET'])
def dummy_view():
    return jsonify(
        {
            "API_URL": "/2/dummy",
            "API_VERSION": 2
        }
    )
