from flask import Flask, render_template, jsonify
import datetime
from DatabaseManager import DatabaseManager

app = Flask(__name__)

db = DatabaseManager("../Common/database.db")

@app.route('/')
def main_view():
    return render_template('main_view.html')

@app.route('/_ajax_chart_hours_')
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

    tempInHourNum = 0
    tempSum = 0

    hourLabel = []
    averageTemps = []

    previousHour = hours[0]
    for i in range(len(temps)):
        if(hours[i] != previousHour):
            averageTemps.append(float(tempSum) / float(tempInHourNum))
            hourLabel.append(previousHour)

            previousHour = hours[i]
            tempSum = 0
            tempInHourNum = 0

        tempSum = tempSum + temps[i]
        tempInHourNum = tempInHourNum + 1

    averageTemps.append(float(tempSum) / float(tempInHourNum))
    hourLabel.append(previousHour)

    return jsonify(isTempsInDatabase=True, hourLabel = hourLabel, temps = averageTemps)
