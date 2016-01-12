from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


from app.v1.views import v1
app.register_blueprint(v1, url_prefix='/1')

from app.v2.views import v2
app.register_blueprint(v2, url_prefix='/2')

from app.v3.views import v3
app.register_blueprint(v3, url_prefix='/3')
