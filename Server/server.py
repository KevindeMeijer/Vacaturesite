from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
# from flask_cors import CORS


# from back_end import word2vec
from back_end.sql_db_connectie import execute_sql, load_sql
from back_end import grafieken

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
    retrieve_reports = load_sql("SELECT * FROM `reports`")
    if retrieve_reports is not None:
        return jsonify(retrieve_reports), 200, {'ContentType': 'application/json'}
    else:
        return jsonify({'success': False}), 400, {'ContentType': 'application/json'}

@app.route("/load_chars_frontend", methods=['GET'])
def load_chars_frontend():
    return jsonify(grafieken.jan_frontend, grafieken.feb_frontend, grafieken.mrt_frontend, grafieken.apr_frontend, grafieken.mei_frontend,
    grafieken.jun_frontend, grafieken.jul_frontend, grafieken.aug_frontend, grafieken.sep_frontend, grafieken.okt_frontend, grafieken.nov_frontend, grafieken.dec_frontend), 200, {'ContentType': 'application/json'}

@app.route("/load_chars_backend", methods=['GET'])
def load_chars_backend():
    return jsonify(grafieken.jan_backend, grafieken.feb_backend, grafieken.mrt_backend, grafieken.apr_backend, grafieken.mei_backend, grafieken.jun_backend,
    grafieken.jul_backend, grafieken.aug_backend, grafieken.sep_backend, grafieken.okt_backend, grafieken.nov_backend, grafieken.dec_backend), 200, {'ContentType': 'application/json'}

@app.route("/load_chars_productowner", methods=['GET'])
def load_chars_productowner():
    return jsonify(grafieken.jan_productowner, grafieken.feb_productowner, grafieken.mrt_productowner, grafieken.apr_productowner, grafieken.mei_productowner, grafieken.jun_productowner,
    grafieken.jul_productowner, grafieken.aug_productowner, grafieken.sep_productowner, grafieken.okt_productowner, grafieken.nov_productowner, grafieken.dec_productowner), 200, {'ContentType': 'application/json'}

@app.route("/load_chars_cloud_security", methods=['GET'])
def load_chars_cloud_security():
    return jsonify(grafieken.jan_cloud_security, grafieken.feb_cloud_security, grafieken.mrt_cloud_security, grafieken.apr_cloud_security, grafieken.mei_cloud_security, grafieken.jun_cloud_security,
    grafieken.jul_cloud_security, grafieken.aug_cloud_security, grafieken.sep_cloud_security, grafieken.okt_cloud_security, grafieken.nov_cloud_security, grafieken.dec_cloud_security), 200, {'ContentType': 'application/json'}

app.run(debug=False)