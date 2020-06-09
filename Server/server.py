from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
# from flask_cors import CORS


# from back_end import word2vec
from back_end.sql_db_connectie import execute_sql, load_sql

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
# @app.route("/ingevoerd", methods=['GET'])
# def ingevoerd():
#     return jsonify(word2vec.goede), 200, {'ContentType': 'application/json'}

@app.route("/report", methods=['POST'])
def report():
    gegevens = request.json
    insert_report = execute_sql("INSERT INTO reports(naam, telefoonnummer, email_adres, onderwerp, bericht) VALUES ('{}', '{}', '{}', '{}', '{}')".format(gegevens['naam'], gegevens['telefoonnummer'], gegevens['email_adres'], gegevens['onderwerp'], gegevens['bericht']))
    if insert_report is None:
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return jsonify({'success': False}), 400, {'ContentType': 'application/json'}

@app.route("/load_reports", methods=['GET'])
def load_reports():
    retrieve_reports = load_sql("SELECT * FROM `reports` WHERE `id_contact`= 1")
    # print(retrieve_reports)
    if retrieve_reports is not None:
        return jsonify(retrieve_reports), 200, {'ContentType': 'application/json'}
        # return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return jsonify({'success': False}), 400, {'ContentType': 'application/json'}

app.run(debug=False)