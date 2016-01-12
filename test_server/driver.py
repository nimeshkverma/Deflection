from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/test_get1', methods=['GET'])
def get_view1():
    print request
    print jsonify({'results': request.args})
    return jsonify({'results': request.args})


@app.route('/test_post1', methods=['POST'])
def post_view1():
    print request.form
    return jsonify({'results': request.form})


@app.route('/test_get2', methods=['GET'])
def get_view2():
    print request.args
    return jsonify({'results': request.args})


@app.route('/test_post2', methods=['POST'])
def post_view2():
    print request.form
    return jsonify({'results': request.form})

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8080")
    )
