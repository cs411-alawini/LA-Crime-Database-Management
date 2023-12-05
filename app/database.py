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
    

# def fetch_descriptions(db):
#     conn = db.connect()
#     query = 'SELECT * FROM CrimeCode;'
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


def fetch_descriptions(description_id, db):
    conn = db.connect()
    query = f'SELECT * FROM CrimeCode WHERE CrimeCodeCode = "{description_id}";'
    query_results = conn.execute(text(query))
    conn.close()
    ret_res = []
    for result in query_results:
        item = {
            "CrimeCode": result[0],
            "CrimeCodeDescription": result[1]
        }
        ret_res.append(item)
    return make_response(jsonify(ret_res), 200)

def fetch_report(db):
    conn = db.connect()
    query = "SELECT * FROM REPORT LIMIT 20;"
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




def insert_new_description(CrimeCode, CrimeCodeDescription, db) -> bool:
    conn = db.connect()
    query = f'INSERT INTO CrimeCode (CrimeCodeCode, CrimeCodeCodeDescription) VALUES ("{CrimeCode}", "{CrimeCodeDescription}");'
    try:
        conn.execute((text(query)))
    except Exception as e:
        conn.close()
        return make_response({"success": False, "response": f"{e}"}, 400)
    conn.close()
    return make_response({"success": True, "response": "Done"}, 200)

def remove_description(description_id, db):
    conn = db.connect()
    query = f'DELETE FROM CrimeCode WHERE CrimeCodeCode = "{description_id}";'
    try:
        conn.execute((text(query)))
    except Exception as e:
        conn.close()
        return make_response({"success": False, "response": f"{e}"}, 400)
    conn.close()
    return make_response({"success": True, "response": "Done"}, 200)

def update_description(description_id, input, db):
    conn = db.connect()
    original_data = conn.execute(f'SELECT * FROM CrimeCode WHERE CrimeCodeCode = "{description_id}";')
    
    if original_data is None:
        return make_response({"success": False, "response": "CrimeCodeCode not found"}, 400)
    
    original_data_dict = original_data.mappings().all()[0]
    crime_code_code = input.get('CrimeCodeCode', original_data_dict["CrimeCodeCode"])
    crime_code_code_description = input.get('CrimeCodeCodeDescription', original_data_dict["CrimeCodeCodeDescription"])
    
    query = f'UPDATE CrimeCode SET CrimeCodeCode = "{crime_code_code}", CrimeCodeCode = "{crime_code_code_description}" WHERE CrimeCodeCode = "{description_id}";'
                
    try:
        conn.execute(query)
    except Exception as e:
        conn.close()
        return make_response({"success": False, "response": f"{e}"}, 400)
    conn.close()
    return make_response({"success": True, "response": "Done"}, 200)