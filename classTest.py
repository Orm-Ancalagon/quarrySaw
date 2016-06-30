import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class LED(object)
	GPIO.setup(8, GPIO.OUT)
	GPIO.setup(10, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(17, GPIO.OUT)
	GPIO.setup(27, GPIO.OUT)
	
	def __init__(self, green, red, white, orange, yellow)
		self.green = green
