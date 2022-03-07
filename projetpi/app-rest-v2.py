#!/usr/bin/python2
# script : app-rest-v2.py
# exec :  FLASK_APP=app-rest-v2.py /home/pi/.local/bin/flask run --host=0.0.0.0
from flask import Flask
from flask import request
import pymongo, pprint
from pymongo import MongoClient
from bson.json_util import dumps
import json
#
client = MongoClient('mongodb://localhost:27017')
db = client.projetpi
#
app = Flask(__name__)
#
#
@app.route("/")
def hello():
    return "Welcome to Python Flask! - saisissez /get_all_captures"
#
#
@app.route("/get_all_captures", methods = ['GET'])
def get_all_captures():
#   try:
    col_captures = db.captures
    mondoc = ""
    for doc in col_captures.find({},{'_id':0, 'date': 1, 'source': 1, 'valeur': 1}):
#       for doc in col_captures.find({}):
        mondoc = dumps(doc) + '</br>' + mondoc
    return mondoc
#
#   except Exception, e:
    return dumps({'error' : str(e)})
