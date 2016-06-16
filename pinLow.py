import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)         # pump
GPIO.setup(7, GPIO.OUT)         # motorUp
GPIO.setup(15, GPIO.OUT)        # motorDown
GPIO.setup(18, GPIO.OUT)        # sawAway
GPIO.setup(22, GPIO.OUT)        # sawTowards

GPIO.output(4, GPIO.HIGH)       # all pins are high at program start
GPIO.output(7, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)

GPIO.cleanup()
