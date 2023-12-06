# import os
# import sqlalchemy
# from flask import Flask

# from flask import Flask, render_template, request, jsonify
# import requests
# from datetime import datetime, timedelta, time
# from database import fetch_descriptions, insert_new_description, remove_description, update_description

# import re
# import json

# app = Flask(__name__)

# def init_connection_engine():
#     """ initialize database setup
#     Takes in os variables from environment if on GCP
#     Reads in local variables that will be ignored in public repository.
#     Returns:
#         pool -- a connection to GCP MySQL
#     """

#     pool = sqlalchemy.create_engine(
#         "mysql+pymysql://root:sqlegends@35.222.239.171/sqlegends"
#     )

#     return pool

# db = init_connection_engine()

# @app.route('/')
# def index():
#     return render_template("temp.html")


# @app.route('/crimeDescription/<int:description_id>', methods=['GET'])
# def check_description(description_id):
#         crimeDescription = fetch_descriptions(description_id, db)
#         return crimeDescription

# @app.route('/crimeDescription/insert', methods=['POST'])
# def insert_description():
#     data = request.get_json()
#     print(data)
#     newCrimeDescription = insert_new_description(data['CrimeCode'], data['CrimeCodeDescription'], db)
#     return newCrimeDescription

# @app.route('/crimeDescription/delete/<int:description_id>', methods=['DELETE'])
# def delete_description(description_id):
#     description = remove_description(description_id, db)
#     return description

# @app.route('/crimeDescription/update/<int:description_id>', methods=['PUT'])
# def update_description(description_id):
#     data = request.get_json()
#     description = update_description(description_id, data, db)
#     return description

import os
import sqlalchemy
from flask import Flask

from flask import Flask, render_template, request, jsonify, render_template_string
import requests
from datetime import datetime, timedelta, time
from database import fetch_descriptions, insert_new_description, remove_description, change_description, stored_procedure, fetch_report

import re
import json
import folium
import pandas as pd

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


# @app.route('/crimeDescription', methods=['GET'])
# def check_description():
#         crimeDescription = fetch_descriptions(db)
        # return crimeDescription
@app.route('/crimeDescription/<int:divisionRecordsNumber>/<int:crimeCode>/<int:area>', methods=['GET'])
def check_description(divisionRecordsNumber,crimeCode, area):
        # divisionRecordsNumber = request.form.get('divisionRecordsNumber')

        # crimeCode = request.form.get('crimeCode')

        # area = request.form.get('area')

        crimeDescription = fetch_descriptions(divisionRecordsNumber,crimeCode, area, db)
        return crimeDescription

# @app.route('/crimeDescription/insert/<int:description_id>', methods=['POST'])
# def insert_description():
#     data = request.form
#     print(f"{data.get('DescriptionIdInsertion')}")
#     print("enter")
#     newCrimeDescription = insert_new_description(data['CrimeCode'], data['CrimeCodeDescription'], db)
#     # newCrimeDescription = insert_new_description(data['C"], "unknown", db)
#     # print(newCrimeDescription)
#     return newCrimeDescription
@app.route('/crimeDescription/insert', methods=['POST'])
def crime_description_insert():
        divisionRecordsNumber = request.form.get('divisionRecordsNumber')
        dateReported = request.form.get('dateReported')
        dateOccurred = request.form.get('dateOccurred')
        timeOccured = request.form.get('timeOccured')
        lat = request.form.get('lat')
        lon = request.form.get('lon')
        crimeCode = request.form.get('crimeCode')
        weaponUsedCode = request.form.get('weaponUsedCode')
        moCodes = request.form.get('moCodes')
        area = request.form.get('area')
        premisesCode = request.form.get('premisesCode')

        result = insert_new_description(divisionRecordsNumber, dateReported, dateOccurred, timeOccured, lat, lon, crimeCode, weaponUsedCode, moCodes, area, premisesCode, db)
        
        return result

@app.route('/crimeDescription/delete/<int:description_id>', methods=['DELETE'])
def delete_description(description_id):
    description = remove_description(description_id, db)
    return description

@app.route('/crimeDescription/update', methods=['PUT'])
def update_description():
    divisionRecordsNumber = request.form.get('divisionRecordsNumber')
    lat2 = request.form.get('lat2')    
    lon2 = request.form.get('lon2')    
    description = change_description(divisionRecordsNumber, lat2, lon2, db)
    return description


@app.route('/generateMap/<int:crimeCode>/<int:area>/<int:limit>', methods =["GET"])
def generateMap(crimeCode, area, limit):
     
    # sql_query_result = pd.DataFrame({
    #     "lat" : [34.0141, 34.0459, 33.9739],
    #     "lon" : [-118.2978, -118.2545, -118.263],
    #     "cc_desc" : ["BATTERY - SIMPLE ASSAULT", "BATTERY - SIMPLE ASSAULT", "VANDALISM - MISDEAMEANOR ($399 OR UNDER)"]
    # })

    report = fetch_report(db, crimeCode, area, limit).get_json()
    print(type(report))
    sql_query_result = pd.DataFrame(report)
    

    # will need to standardize how to store the records

    # the popup can also be written as html code. you can add bullets and other items as needed ("<br><br>" for newline)

    map_center = [34.052235, -118.243683]
    map = folium.Map(location=map_center, zoom_start=10)

    for index, row in sql_query_result.iterrows():
        folium.Marker(location=[row["lat"], row["lon"]], popup="Time: " + str(row["timeOccurred"])).add_to(map)

    map_html = map.get_root().render()
    return render_template_string('<div>{{ map_html|safe }}</div>', map_html=map_html)

@app.route('/storedProcedure/<string:year>/<string:area>/<string:description>')
def call_stored_procedure(year, area, description):
    response = stored_procedure(year, area, description, db)
    return response.get_json()