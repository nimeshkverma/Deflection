from flask import jsonify, request


def dummy_get_view(request):
    return jsonify(
        {
            "API_URL": "/3/dummy_get",
            "API_VERSION": 3,
            "API_METHOD": "GET",
        }
    )


def dummy_post_view(request):
    return jsonify(
        {
            "API_URL": "/3/dummy_post",
            "API_VERSION": 3,
            "API_METHOD": "POST",
        }
    )
