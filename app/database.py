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
    

def fetch_descriptions(db):
    conn = db.connect()
    query = 'SELECT * FROM CrimeCode;'
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
