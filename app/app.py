import os
import sqlalchemy
from flask import Flask

from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta, time

import re
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("temp.html")

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
