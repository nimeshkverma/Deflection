import os
import sys

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


from app.authorisation.views import authorisation as authorisationModule
app.register_blueprint(authorisationModule)