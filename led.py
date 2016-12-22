import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
print "RED on"
GPIO.output(18, GPIO.HIGH)
time.sleep(3)
print "RED off"
GPIO.output(18, GPIO.LOW)

GPIO.setup(23, GPIO.OUT)
print "GREEN on"
GPIO.output(23, GPIO.HIGH)
time.sleep(3)
print "GREEN off"
GPIO.output(23, GPIO.LOW)

