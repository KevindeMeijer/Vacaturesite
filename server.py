import http.server
import socketserver
from flask import Flask, request, jsonify, redirect, render_template
from flask_cors import CORS

from nosql_db_connectie import goed

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

app.run()

@app.route("/ingevoerd")
def ingevoerd():
    return jsonify(goed), 200, {'ContentType': 'application/json'}

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("servering at port", PORT)
    httpd.serve_forever()
