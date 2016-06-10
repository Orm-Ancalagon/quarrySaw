from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


measurement = input("Please enter you number here: ")
measurement = float(measurement) 
try:
	float(measurement)
except ValueError:
	print("you need to enter a floating-point number")

GPIO.output(17, GPIO.HIGH)
sleep(measurement)
GPIO.output(17, GPIO.LOW)
GPIO.cleanup()
