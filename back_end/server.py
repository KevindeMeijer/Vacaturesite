import http.server
import socketserver
from flask import Flask, request, jsonify, redirect

from nosql_db_connectie import goed

app = Flask(__name__)

@app.route('/ingevoerd', methods= ['GET'])
def ingevoerd():
    return jsonify(goed), 200, {'ContentType': 'application/json'}





PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("servering at port", PORT)
    httpd.serve_forever()
