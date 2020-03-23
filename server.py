from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
# from flask_cors import CORS

from nosql_db_connectie import goed

app = Flask(__name__)
# CORS(app)

# webserver
@app.route("/")
def index():
    return send_from_directory('html', 'home2.html')

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


# api bezig
# @app.route("/")
# def 

@app.route("/ingevoerd", methods=['GET'])
def ingevoerd():
    return jsonify(goed), 200, {'ContentType': 'application/json'}



app.run()