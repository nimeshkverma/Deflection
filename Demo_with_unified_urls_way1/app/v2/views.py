from flask import jsonify, request

from utils import get_response


def dummy_view(request):
    response = get_response(request)
    return jsonify(response)
