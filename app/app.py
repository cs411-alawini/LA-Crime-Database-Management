import os
import sqlalchemy
from flask import Flask

from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta, time
from database import fetch_descriptions, insert_new_description, remove_description, update_description

import re
import json

app = Flask(__name__)

def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """

    pool = sqlalchemy.create_engine(
        "mysql+pymysql://root:sqlegends@35.222.239.171/sqlegends"
    )

    return pool

db = init_connection_engine()

@app.route('/')
def index():
    return render_template("temp.html")


@app.route('/crimeDescription/<int:description_id>', methods=['GET'])
def check_description(description_id):
        crimeDescription = fetch_descriptions(description_id, db)
        return crimeDescription

@app.route('/crimeDescription/insert', methods=['POST'])
def insert_description():
    data = request.get_json()
    print(data)
    newCrimeDescription = insert_new_description(data['CrimeCode'], data['CrimeCodeDescription'], db)
    return newCrimeDescription

@app.route('/crimeDescription/delete/<int:description_id>', methods=['DELETE'])
def delete_description(description_id):
    description = remove_description(description_id, db)
    return description

@app.route('/crimeDescription/update/<int:description_id>', methods=['PUT'])
def update_description(description_id):
    data = request.get_json()
    description = update_description(description_id, data, db)
    return description