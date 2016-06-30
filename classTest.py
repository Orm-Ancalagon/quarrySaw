from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class LED(object):
	GPIO.setup(4, GPIO.OUT)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	
	GPIO.output(4, GPIO.HIGH) # high = off
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)

	
	def __init__(self, yellow, orange, green, red, white):
		self.yellow = 	GPIO.output(4, yellow)
		self.orange = 	GPIO.output(7, orange)
		self.green  = 	GPIO.output(15, green)
		self.red    = 	GPIO.output(18, red)
		self.white  =	GPIO.output(22, white)

yellowLED = LED(GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH)
sleep(3)

orangeLED = LED(GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.HIGH)
sleep(3)

greenLED = LED(GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.HIGH)
sleep(3)


GPIO.cleanup()	
		
