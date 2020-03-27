from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
# from flask_cors import CORS


from back_end import word2vec


app = Flask(__name__)
# CORS(app)

# webserver
@app.route("/")
def index():
    return send_from_directory('html', 'home.html')

@app.route('/<path:path>')
def send_html(path):
    return send_from_directory('html', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route("/ingevoerd", methods=['GET'])
def ingevoerd():
    return jsonify(word2vec.output), 200, {'ContentType': 'application/json'}



app.run()