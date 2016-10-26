import sqlite3
import datetime

class DatabaseManager:

    def __init__(self, databasePath):
        self.databasePath = databasePath
        self.formatString = "%Y-%m-%d %H:%M:%S"

    def insertTemperature(self, temperature):
        conn = sqlite3.connect(self.databasePath)

        dtime = datetime.datetime.now()
        dateTimeString = dtime.strftime(self.formatString)

        conn.execute("INSERT INTO temp VALUES ('" + dateTimeString + "',{})".format(temperature)  )

        conn.commit()
        conn.close()

    def selectTemperatureBetween(self, startDateTime, endDateTime):
        sDTimeString = startDateTime.strftime(self.formatString)
        eDTimeString = endDateTime.strftime(self.formatString)

        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute(\
            "SELECT dtime, temperature FROM temp WHERE \
            dtime >= ? AND dtime <= ?", (sDTimeString, eDTimeString))

        datetime_data = []
        temperature_data = []

        for row in cursor:
            dt = datetime.datetime.strptime(row[0], self.formatString)
            datetime_data.append(dt)
            temperature_data.append(int(row[1]))


        conn.commit()
        conn.close()
        return datetime_data, temperature_data

    def selectLastTemperature(self):

        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute("SELECT temperature FROM temp WHERE dtime = \
        (SELECT MAX(dtime) FROM temp)")

        temperature = 0
        for c in cursor:
            temperature = int(c[0])

        #dt = datetime.datetime.strptime(row[0], self.formatString)

        conn.commit()
        conn.close()
        return temperature

    def selectConfig(self):
        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute("SELECT desiredTemp FROM conf");

        desiredTemperature = 0

        for c in cursor:
            desiredTemperature = c[0]


        conn.commit()
        conn.close()
        return desiredTemperature

    def updateConfig(self, newDesiredTemperature):
        conn = sqlite3.connect(self.databasePath)

        conn.execute("DELETE FROM conf")

        conn.execute("INSERT INTO conf VALUES({})".format(newDesiredTemperature))

        conn.commit()
        conn.close()

