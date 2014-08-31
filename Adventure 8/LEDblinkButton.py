import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

while True:
  if GPIO.input(24):
    GPIO.output(23, True)
  else:
    GPIO.output(23, False)
  time.sleep(0.1)
