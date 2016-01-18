from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config')

from app.v1.views import v1
from app.v2.views import v2
from app.v3.views import v3

VERSION_OBJECT_MAPPING = {
    '1': v1,
    '2': v2,
    '3': v3,
}


def get_url_prefix(version):
    return '/' + str(version)


def register_versions(allowed_versions):
    for version in allowed_versions:
        app.register_blueprint(
            VERSION_OBJECT_MAPPING[version], url_prefix=get_url_prefix(version))


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Message": "URL not supported"}), 404
