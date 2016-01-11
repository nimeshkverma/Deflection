from flask import Blueprint, request, redirect, url_for, jsonify
import mappings

authorisation = Blueprint('authorisation', __name__)

@authorisation.route('/<int:version>/signin/', methods=['POST'])
def signin(version):
    print jsonify({'nimesh':request.form}), version
    return redirect(mappings.DESTINATION['/signin/'][version], 301)

@authorisation.route('/<int:version>/signup/', methods=['GET'])
def signup(version):
    print  jsonify({'nimesh':request.args}), version, version
    return redirect(mappings.DESTINATION['/signin/'][version], 301)