from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.v1.urls import v1
from app.v2.urls import v2
from app.v3.urls import v3

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
