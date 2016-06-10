from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


measurement = input("Please enter you number here: ")
measurement = float(measurement) 

GPIO.output(17, GPIO.HIGH)
sleep(measurement)
GPIO.output(17, GPIO.LOW)
GPIO.cleanup()
