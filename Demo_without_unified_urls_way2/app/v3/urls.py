from flask import Blueprint
from views import dummy_get_view, dummy_post_view

v3 = Blueprint('v3', __name__)

v3.add_url_rule('/dummy_post', view_func=dummy_post_view, methods=['POST'])
v3.add_url_rule('/dummy_get', view_func=dummy_get_view, methods=['GET'])
