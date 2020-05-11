from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
# from flask_cors import CORS


from back_end import word2vec


app = Flask(__name__)
# CORS(app)

# webserver
@app.route("/")
def index():
    return send_from_directory('html', 'index.html')

@app.route('/html/<path:filename>')
def send_html(filename):
    return send_from_directory('html', filename)

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory('js', filename)

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('css', filename)

@app.route('/img/<path:filename>')
def send_img(filename):
    return send_from_directory('img', filename)

#API Routes
@app.route("/ingevoerd", methods=['GET'])
def ingevoerd():
    return jsonify(word2vec.goede), 200, {'ContentType': 'application/json'}



app.run(debug=False)