import time
from w1thermsensor import W1ThermSensor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from DatabaseManager import DatabaseManager
from Heater import Heater

class Driver:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.db = DatabaseManager('/home/pi/sfc/Common/database.db')
        self.sensor = W1ThermSensor()
        self.heater = Heater()

        self.checkFrequency()
        self.checkMinMaxTemperature()

        self.scheduler.start()
        self.initSchedulers()

    def initSchedulers(self):
        self.lt = self.scheduler.add_job(self.logTemperature, 'interval', seconds=self.frequency)
        self.uc = self.scheduler.add_job(self.updateConditional, 'interval', seconds=self.frequency)
        self.ch = self.scheduler.add_job(self.controlHeater, 'interval', seconds=self.frequency)

    def run(self):
        print('*** Press CTRL-C to exit. ***')

        try:
            while True:
                time.sleep(3)

        except(KeyboardInterrupt, SystemExit):
            print('*** Bye, bye. ***')
            self.scheduler.shutdown()

    def logTemperature(self):
        self.db.insertTemperature(self.sensor.get_temperature())
        
    def checkFrequency(self):
        self.frequency = self.db.selectFrequencyFromConf()

    def checkMinMaxTemperature(self):
        [self.minTemperature, self.maxTemperature] = self.db.selectMinAndMaxTempFromConf()

    def updateConditional(self):
        self.checkMinMaxTemperature()
       
        f = self.db.selectFrequencyFromConf()
        
        if(self.frequency != f):
            self.frequency = f

            self.lt.remove()
            self.lt = self.scheduler.add_job(self.logTemperature, 'interval', seconds=self.frequency)

            self.uc.remove()
            self.uc = self.scheduler.add_job(self.updateConditional, 'interval', seconds=self.frequency)

            self.ch.remove()
            self.ch = self.scheduler.add_job(self.controlHeater, 'interval', seconds=self.frequency)

    def controlHeater(self):
        avg = self.db.selectAverageLastFive()

        if avg < self.minTemperature:
            self.heater.on()
        elif avg > self.maxTemperature:
            self.heater.off()

if __name__ == '__main__':
    d = Driver()
    d.run()
