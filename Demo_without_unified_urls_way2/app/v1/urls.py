from flask import Blueprint
from views import dummy_view

v1 = Blueprint('v1', __name__)

v1.add_url_rule('/dummy_post', view_func=dummy_view, methods=['POST'])
v1.add_url_rule('/dummy_get', view_func=dummy_view, methods=['GET'])
