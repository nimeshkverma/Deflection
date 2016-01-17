from flask import jsonify


def dummy_get_view():
    return jsonify(
        {
            "API_URL": "/3/dummy",
            "API_VERSION": 3,
            "API_METHOD": "GET",
        }
    )


def dummy_post_view():
    return jsonify(
        {
            "API_URL": "/3/dummy",
            "API_VERSION": 3,
            "API_METHOD": "POST",
        }
    )
