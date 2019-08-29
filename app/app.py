from flask import Flask, make_response, request , jsonify, render_template      
import os, json 
import flask as fl
import sys, zipfile, io , pathlib
sys.path.append('../')
from plutarchus.build_website import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', methods=['GET',"POST"])
def transform_view():
    request_file = request.files['data_file']

    if not request_file:
        return "No file"

    request_file.save('temp.json')

    with open('temp.json') as json_file:  
        data_file= json.load(json_file)
    os.system('rm temp.json')
    os.system("cp -r assets/themes/"+ data_file["basics"]["theme"]+" website")
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
