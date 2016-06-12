from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

measurement = 0

def getMeasurement():
	while True:
		try:
			global measurement
			measurement = input("Please enter you number here: ")
			measurement = float(measurement)
		except ValueError:
			print("you need to enter a floating-point number")
			continue
		else:
			break

def powerPin():
	GPIO.output(17, GPIO.HIGH)
	sleep(measurement*2)
	GPIO.output(17, GPIO.LOW)

getMeasurement()
powerPin()
GPIO.cleanup() 
