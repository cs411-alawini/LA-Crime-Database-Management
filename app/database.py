"""Defines all the functions related to the database"""
import string
import random
from flask import jsonify, make_response
from sqlalchemy import text

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    

def fetch_descriptions(divisionRecordsNumber, crime_id, area_id, db):
    conn = db.connect()
    # query = f'SELECT * FROM CrimeCode WHERE CrimeCodeCode = "{description_id}";'
    query = f'SELECT * FROM Report WHERE divisionRecordsNumber = "{divisionRecordsNumber}" OR crimeCode = "{crime_id}" OR area = "{area_id}";'

    query_results = conn.execute(text(query))
    conn.close()
    ret_res = []
    for result in query_results:
        item = {
            "divisionRecordsNumber": result[0],
            "dateReported": result[1],
            "dateOccurred": result[2],
            "timeOccured": result[3],
            "lat": result[4],
            "lon": result[5],
            "crimeCode": result[6],
            "weaponUsedCode": result[7],
            "moCodes": result[8],
            "area": result[9],
            "premisesCode": result[10],
        }
        ret_res.append(item)
    return make_response(jsonify(ret_res), 200)

# def fetch_descriptions(db):
#     conn = db.connect()
#     query = f'SELECT * FROM CrimeCode;'
#     query_results = conn.execute(text(query))
#     conn.close()
#     ret_res = []
#     for result in query_results:
#         item = {
#             "CrimeCode": result[0],
#             "CrimeCodeDescription": result[1]
#         }
#         ret_res.append(item)
#     return make_response(jsonify(ret_res), 200)

# divisionRecordsNumber, dateReported, dateOccurred, timeOccured, lat, lon, crimeCode, weaponUsedCode, moCodes, area, premisesCode
# def insert_new_description(CrimeCode, CrimeCodeDescription, db) -> bool:
def insert_new_description(divisionRecordsNumber, dateReported, dateOccurred, timeOccured, lat, lon, crimeCode, weaponUsedCode, moCodes, area, premisesCode, db) -> bool:
    conn = db.connect()
    # print("pre-insert")
    # query = f'INSERT INTO CrimeCode (CrimeCodeCode, CrimeCodeCodeDescription) VALUES ("{CrimeCode}", "{CrimeCodeDescription}");'
    query = f'INSERT INTO Report (divisionRecordsNumber, dateReported, dateOccurred, timeOccured, lat, lon, crimeCode, weaponUsedCode, moCodes, area, premisesCode) VALUES ("{divisionRecordsNumber}", "{dateReported}", "{dateOccurred}", "{timeOccured}", "{lat}", "{lon}", "{crimeCode}", "{weaponUsedCode}", "{moCodes}", "{area}", "{premisesCode}");'

    try:
        conn.execute((text(query)))
    except Exception as e:
        conn.close()
        return make_response({"success": False, "response": f"{e}"}, 400)
    conn.commit()

    conn.close()
    # print(f"{CrimeCode} has been added")
    return make_response({"success": True, "response": "Done"}, 200)

def remove_description(description_id, db):
    conn = db.connect()
    # print("pre-Delete")
    # query = f'DELETE FROM CrimeCode WHERE CrimeCodeCode = "{description_id}";'
    query = f'DELETE FROM Report WHERE divisionRecordsNumber = "{description_id}";'

    try:
        conn.execute((text(query)))
    except Exception as e:
        conn.close()
        return make_response({"success": False, "response": f"{e}"}, 400)
    conn.commit()
    conn.close()
    print("post-Delete")

    return make_response({"success": True, "response": "Done"}, 200)

def change_description(divisionRecordsNumber, lat2, lon2, db):
    conn = db.connect()
    # original_data = conn.execute(text(f'SELECT * FROM CrimeCode WHERE CrimeCodeCode = "{description_id}";'))
    original_data = conn.execute(text(f'SELECT * FROM Report WHERE divisionRecordsNumber = "{divisionRecordsNumber}";'))

    
    if original_data is None:
        return make_response({"success": False, "response": "CrimeCodeCode not found"}, 400)
    

    query = f'UPDATE Report SET lat = "{lat2}" WHERE divisionRecordsNumber = "{divisionRecordsNumber}";'
    query2 = f'UPDATE Report SET lon = "{lon2}" WHERE divisionRecordsNumber = "{divisionRecordsNumber}";'

    try:
        conn.execute(text(query))
        conn.execute(text(query2))
        conn.commit()
    except Exception as e:
        conn.close()
        return make_response({"success": False, "response": f"{e}"}, 400)
    conn.close()
    return make_response({"success": True, "response": "Done"}, 200)

def fetch_report(db, crimeCode, area, limit):
    conn = db.connect()
    crimeCode_in = str(crimeCode)
    area_in = str(area)
    limit_in = str(limit)
    query = f'SELECT * FROM Report WHERE crimeCode = {crimeCode_in} AND area = {area_in} LIMIT {limit_in};'
    query_results = conn.execute(text(query))
    conn.close
    ret_res = []
    for result in query_results:
        item = {
                "divisionRecordsNumber" : result[0],
                "dateReported" : result[1],
                "dateOccurred" : result[2],
                "timeOccurred" : result[3],
                "lat" : result[4],
                "lon" : result[5],
                "crimCode" : result[6],
                "weaponUsedCode" : result[7],
                "moCodes" : result[8],
                "area" : result[9],
                "premisesCode" : result[10]
        }
        ret_res.append(item)
    return make_response(jsonify(ret_res), 200)

def stored_procedure(year, area, description, db):
    conn = db.connect()
    query = f'CALL delete_rows("{year}", "{area}", "{description}");'
    result = ''
    try:
        results = conn.execute((text(query)))
    except Exception as e:
        conn.close()
        return make_response({"success": False, "response": f"{e}"}, 400)
    conn.commit()
    conn.close()
    ret_res = []
    for result in results:
        item = {
            "Area": result[0],
            "Nummber of reports": result[1]
        }
        ret_res.append(item)

    return make_response(jsonify(ret_res), 200)