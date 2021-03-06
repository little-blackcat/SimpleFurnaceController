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

        conn.commit()
        conn.close()
        return temperature
        
    def selectLastTenTemperatures(self):
        
        conn = sqlite3.connect(self.databasePath)
        
        cursor = conn.execute("SELECT * FROM temp ORDER BY dtime DESC LIMIT 10")

        datetime_data = []
        temperature_data = []

        for row in cursor:
            dt = datetime.datetime.strptime(row[0], self.formatString)
            datetime_data.append(dt)
            temperature_data.append(int(row[1]))

        conn.commit()
        conn.close()
        return datetime_data, temperature_data
        
        

    def selectAverageLastFive(self):
        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute("SELECT AVG(temperature) FROM (SELECT temperature FROM temp ORDER BY dtime DESC LIMIT 5)")
        avg = cursor.fetchone()[0]

        conn.close()
        return avg

    def selectMinAndMaxTempFromConf(self):
        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute("SELECT minTemp, maxTemp FROM conf");

        row = cursor.fetchone()
        minTemp = row[0]
        maxTemp = row[1]

        conn.commit()
        conn.close()

        return minTemp, maxTemp
        
    def selectMinTempFromConf(self):
        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute("SELECT minTemp FROM conf");
        row = cursor.fetchone()
        minTemp = row[0]
        
        conn.commit()
        conn.close()

        return minTemp
        
    def selectMaxTempFromConf(self):
        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute("SELECT maxTemp FROM conf");
        row = cursor.fetchone()
        maxTemp = row[0]
        
        conn.commit()
        conn.close()

        return maxTemp
        
    def selectFrequencyFromConf(self):
        conn = sqlite3.connect(self.databasePath)

        cursor = conn.execute("SELECT frequency FROM conf");

        frequency = cursor.fetchone()[0]

        conn.commit()
        conn.close()

        return frequency

    def updateConfig(self, newMinTemperature, newMaxTemperature, newFrequency):
        conn = sqlite3.connect(self.databasePath)

        conn.execute("DELETE FROM conf")

        conn.execute("INSERT INTO conf VALUES({}, {}, {})".format(newMinTemperature, newMaxTemperature, newFrequency))

        conn.commit()
        conn.close()
        
    def updateMinTemp(self, newMinTemperature):
        conn = sqlite3.connect(self.databasePath)
        
        conn.execute("UPDATE conf SET minTemp={}".format(newMinTemperature))
        
        conn.commit()
        conn.close()
        
    def updateMaxTemp(self, newMaxTemperature):
        conn = sqlite3.connect(self.databasePath)
        
        conn.execute("UPDATE conf SET maxTemp={}".format(newMaxTemperature))
        
        conn.commit()
        conn.close()
        
    def updateFrequency(self, newFrequency):
        conn = sqlite3.connect(self.databasePath)
        
        conn.execute("UPDATE conf SET frequency={}".format(newFrequency))
        
        conn.commit()
        conn.close()

