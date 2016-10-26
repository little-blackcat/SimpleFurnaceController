import time
from w1thermsensor import W1ThermSensor
from apscheduler.schedulers.background import BackgroundScheduler

from DatabaseManager import DatabaseManager
from Heater import Heater


def logTemperature():
  db.insertTemperature(sensor.get_temperature())


def heaterController():
  avg = db.selectAverageLastFive()
  if avg < 22:
    heater.on()
  elif avg > 27:
    heater.off()


if __name__ == '__main__':
  scheduler = BackgroundScheduler()

  db = DatabaseManager('test.db')
  sensor = W1ThermSensor()
  heater = Heater()

  scheduler.add_job(logTemperature, 'interval', seconds=5)
  scheduler.add_job(heaterController, 'interval', seconds=5)

  scheduler.start()

  print('*** Press Ctrl-C to exit. ***')

  try:
    while True:
      time.sleep(3)

  except(KeyboardInterrupt, SystemExit):
    print('*** Bye, Bye ***')
    scheduler.shutdown()
