import RPi.GPIO as gpio

class Heater:
  def __init__(self):
    self.pin = 18
    gpio.setmode(gpio.BCM)
    gpio.setup(self.pin, gpio.OUT)

  def __del__(self):
    gpio.cleanup()

  def on(self):
    gpio.output(self.pin, gpio.HIGH)

  def off(self):
    gpio.output(self.pin, gpio.LOW)
