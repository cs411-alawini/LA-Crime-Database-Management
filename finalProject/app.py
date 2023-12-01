from flask import Flask, render_template, request, jsonify
import os
import requests
from datetime import datetime, timedelta, time

import re
import json

app = Flask(__name__)

caching = {"Info": None}


# Route for "/" (frontend):
@app.route('/')
def index():
    return render_template("index.html")


def day_and_time(course):
    server_url = os.getenv('COURSES_MICROSERVICE_URL')

    cl = re.split(r"(\d+)", course)

    if cl[0][-1] == ' ':
        cl[0] = cl[0][:-1]

    subject = cl[0].upper()
    course_number = cl[1]

    r = requests.get(f'{server_url}/{subject}/{course_number}').json()
    return r


# Route for "/weather" (middleware):
@app.route('/weather', methods=["POST"])
def POST_weather():
    course = request.form["course"]

    server_url = os.getenv('COURSES_MICROSERVICE_URL')

    cl = re.split(r"(\d+)", course)

    if cl[0] and cl[0][-1] == ' ':
        cl[0] = cl[0][:-1]

    subject = cl[0].upper()
    course_number = ""

    if (len(cl) > 1 and subject.isalpha()):

        course_number = cl[1]
        course = subject + " " + course_number
    else:
        course = subject

    r = requests.get(f'{server_url}/{subject}/{course_number}')

    if (r.status_code == 404):
        return_data = {
            "course": course,
            "nextCourseMeeting": "",
            "forecastTime": "",
            "temperature": "",
            "shortForecast": ""
        }
        return jsonify(return_data), 400

    nextCourseMeeting = ""
    forecastTime = ""
    temperature = 0
    shortForecast = ""

    diff = 0

    microservice_json = day_and_time(course)  # this is already a json file

    days = microservice_json["Days of Week"]
    time = microservice_json["Start Time"]

    # changing 12 hour format to 24 hour format
    time_24 = convert_twenty_four(time)

    current_date = datetime.now()

    current_day = current_date.strftime('%A')

    current_time = current_date.time()

    temp_date = current_date

    if (current_day == "Monday"):
        current_day = 0
    if (current_day == "Tuesday"):
        current_day = 1
    if (current_day == "Wednesday"):
        current_day = 2
    if (current_day == "Thursday"):
        current_day = 3
    if (current_day == "Friday"):
        current_day = 4
    if (current_day == "Saturday"):
        current_day = 5
    if (current_day == "Sunday"):
        current_day = 6

    days_list = []
    for i in days:
        if (i is 'M'):
            days_list.append(0)
        if (i is 'T'):
            days_list.append(1)
        if (i is 'W'):
            days_list.append(2)
        if (i is 'R'):
            days_list.append(3)
        if (i is 'F'):
            days_list.append(4)
        if (i is 'S'):
            days_list.append(5)
        if (i is 'U'):
            days_list.append(6)

    days_list.append(7 + days_list[0])

    index = -1

    if (current_day in days_list):
        index = days_list.index(current_day)

    course_timing = time_24.time()  # getting the course time

    if (index != -1 and course_timing >= current_time):

        temp_date = str(current_date)
        temp_date = temp_date[:10]
        course_timing = str(course_timing)
        nextCourseMeeting = temp_date + " " + course_timing

    elif (index != -1 and course_timing < current_time):

        index += 1
        diff = days_list[index] - days_list[index - 1]
        current_date += timedelta(days=diff)

        temp_date = str(current_date)
        temp_date = temp_date[:10]
        course_timing = str(course_timing)
        nextCourseMeeting = temp_date + " " + course_timing

    elif (index == -1):

        for i in range(len(days_list)):
            if (days_list[i] > current_day):
                diff = days_list[i] - current_day
                break

        current_date += timedelta(days=diff)
        temp_date = str(current_date)
        temp_date = temp_date[:10]
        course_timing = str(course_timing)
        nextCourseMeeting = temp_date + " " + course_timing

    nextCourseMeeting_obj = datetime.strptime(
        nextCourseMeeting, '%Y-%m-%d %H:%M:%S')  # storing nextCourseMeeting as a datetime obj

    available = True

    if (diff >= 6):

        forecastTime = nextCourseMeeting
        temperature = "forecast unavailable"
        shortForecast = "forecast unavailable"

        available = False

    if (caching["Info"] == None):
        forecast = get_coords_and_forecast()  # this is already a json file
        caching["Info"] = forecast
        # print(caching["Info"])

    forecast = caching["Info"]

    for i in range(len(forecast["properties"]["periods"])):

        if (available is False):
            break

        # Get the forecast for the ith hour
        forecast_hour = forecast["properties"]["periods"][i]
        # Get the datetime of the forecast for the ith hour
        hour_start_time = datetime.fromisoformat(
            forecast_hour["startTime"][:19])
        hour_end_time = datetime.fromisoformat(forecast_hour["endTime"][:19])

        if (nextCourseMeeting_obj >= hour_start_time and nextCourseMeeting_obj < hour_end_time):
            nextCourseMeeting = nextCourseMeeting
            forecastTime = forecast_hour["startTime"][:19].replace("T", " ")
            temperature = forecast_hour["temperature"]
            shortForecast = forecast_hour["shortForecast"]

            break

    return_data = {
        "course": course,
        "nextCourseMeeting": nextCourseMeeting,
        "forecastTime": forecastTime,
        "temperature": temperature,
        "shortForecast": shortForecast
    }

    return jsonify(return_data), 200


def convert_twenty_four(time):
    # Parse the time string into a datetime object
    t = datetime.strptime(time, '%I:%M %p')
    # Format the datetime object into a 24-hour time string
    new_time = t.strftime('%H:%M')

    return datetime.strptime(new_time, '%H:%M')  # returning a datetime object


def get_coords_and_forecast():
    grids = requests.get("https://api.weather.gov/points/40.1125,-88.2284")
    grids = grids.json()

    wfo = grids["properties"]["gridId"]
    gridX = grids["properties"]["gridX"]
    gridY = grids["properties"]["gridY"]

    r = requests.get(
        f"https://api.weather.gov/gridpoints/{wfo}/{gridX},{gridY}/forecast/hourly").json()
    return r


# Route for "/weatherCache" (middleware/backend):
@app.route('/weatherCache')
def get_cached_weather():
    # ...

    if (caching["Info"] == None):
        return {}
    else:
        return caching["Info"]


# temp_start_time = forecast_hour["startTime"][:19].replace("T", " ")
# temp_end_time = forecast_hour["endTime"][:19].replace("T", " ")

# print(temp_start_time)

# temp_start = datetime.strptime(
#     temp_start_time, '%Y-%m-%d %H:%M:%S')

# print(temp_start)

# temp_end = datetime.strptime(
#     temp_end_time, '%Y-%m-%d %H:%M:%S')

# hour_start_time = datetime.fromisoformat(
#     temp_start_time)
# hour_end_time = datetime.fromisoformat(temp_end_time)

# print(hour_start_time)
