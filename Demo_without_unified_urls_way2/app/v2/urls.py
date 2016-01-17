from flask import Blueprint
from views import dummy_view

v2 = Blueprint('v2', __name__)

v2.add_url_rule('/dummy_post', view_func=dummy_view, methods=['POST'])
v2.add_url_rule('/dummy_get', view_func=dummy_view, methods=['GET'])
