from flask import Blueprint, jsonify

v3 = Blueprint('v3', __name__)


def dummy_get_view():
    return jsonify(
        {
            "API_URL": "/3/dummy_get",
            "API_VERSION": 3,
            "API_METHOD": "GET",
        }
    )


def dummy_post_view():
    return jsonify(
        {
            "API_URL": "/3/dummy_post",
            "API_VERSION": 3,
            "API_METHOD": "POST",
        }
    )
