from flask import Flask, render_template, jsonify
import datetime
from DatabaseManager import DatabaseManager

from GroupAverage import groupAndAverage

app = Flask(__name__)

db = DatabaseManager("../Common/database.db")

@app.route('/')
def home_view():
    return render_template('home_view.html')

@app.route('/half-day')
def half_day_view():
    return render_template('half_day_view.html')

@app.route('/hour')
def hour_view():
    return render_template('hour_view.html')

@app.route('/_ajax_chart_halfday_')
def _ajax_chart_hours_():
    now = datetime.datetime.now()
    before = datetime.datetime.now() - datetime.timedelta(hours=12)

    dtimes, temps = db.selectTemperatureBetween(before, now)

    if(len(dtimes) == 0):
        print("ERROR")
        return jsonify(isTempsInDatabase=False)

    hours = []
    for d in dtimes:
        hours.append( d.hour )

    hourLabel, averageTemps = groupAndAverage(hours, temps)

    return jsonify(isTempsInDatabase=True, hourLabel = hourLabel, temps = averageTemps)

@app.route('/_ajax_chart_last_hour_')
def _ajax_chart_last_hour_():

    now = datetime.datetime.now()
    before = datetime.datetime.now() - datetime.timedelta(hours=1)

    dtimes, temps = db.selectTemperatureBetween(before, now)

    if(len(dtimes) == 0):
        print("ERROR")
        return jsonify(isTempsInDatabase=False)

    minutes = []

    for d in dtimes:
        minutes.append(d.minute)

    labels, averages = groupAndAverage(minutes, temps)

    return jsonify(isTempsInDatabase=True, minuteLabel = labels, temps = averages)


