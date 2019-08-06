from flask import Flask, make_response, request , jsonify, render_template      
import os, json 
import flask as fl
import sys, zipfile, io , pathlib

from build_funcs import build_website

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/transform', methods=['GET',"POST"])
def transform_view():
    request_file = request.files['data_file']

    if not request_file:
        return "No file"

    request_file.save('temp.json')

    with open('temp.json') as json_file:  
        data_file= json.load(json_file)
    os.system('rm temp.json')

    build_website(data_file)

    os.system('zip -r website.zip website')
    os.system('rm -rf website')

    data = open('website.zip', 'rb')

    data.seek(0)

    os.system("rm -rf website.zip")

    return fl.send_file(
        data,
        mimetype='application/zip',
        as_attachment=True,
        attachment_filename='website.zip'
    )


       # base_path = pathlib.Path('./website/')
    # data = io.BytesIO()
    # with zipfile.ZipFile(data, mode='w') as z:
    #     for f_name in base_path.iterdir():
    #         z.write(f_name)