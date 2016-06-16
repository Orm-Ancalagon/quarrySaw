from time import sleep		# import the sleep function from the time module
import RPi.GPIO as GPIO		# GPIO module

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)		# pump
GPIO.setup(7, GPIO.OUT)		# motorUp
GPIO.setup(15, GPIO.OUT)	# motorDown
GPIO.setup(18, GPIO.OUT)	# sawAway
GPIO.setup(22, GPIO.OUT)	# sawTowards

GPIO.output(4, GPIO.HIGH)	# all pins are high at program start
GPIO.output(7, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)

measurement = "blank"
motionTime = "blank"
passesNumber = 0
begin = 0

def howMuchToCut():		# function asks measurement and checks if input is a number
	while True:
		try:
			global measurement
			measurement = input("Please enter your measurement here: \n")
			measurement = float(measurement)
		except ValueError:
			print("Invalid entry, please enter a number: \n")
			continue
		else:
			break    

def travelTime():		# how long the saw takes to travel across the block
	while True:
		try:
			global motionTime
			motionTime = input("Please enter traveltime in seconds: \n")
			motionTime = float(motionTime)
		except ValueError:
			print(motionTime, "is not a valid input, please re-enter: \n")
			continue
		else:
			break

def passes():			# number of times the saw moves away and towards
	while True:
                try:
                        global passesNumber
                        passesNumber = input("Please enter number of passes: \n")
                        passesNumber = int(passesNumber)
                except ValueError:
                        print(passesNumber, "is not a valid number of passes, please re-enter: \n")
                        continue
                else:
                        break

def ynQuery():			# confirm entered depth and query to proceed
	list = [measurement, motionTime, passesNumber]
	print("You have entered:\n")
	print ("\n".join(map(str,list)))

	start = input("\nDo you wish to begin cutting? (y/n)")
	str(start)
	
	if start == "y":
		global begin
		begin = 1
		print("Cutting at", measurement, "mm")
		print("Travel time is", motionTime, "s")

	if start == "n":
		print("Cut canceled")

	elif start != "y" and "n":
		print("invalid input, please enter y/n")

def pumpOn():
	GPIO.output(4, GPIO.LOW)

def pumpOff():
	GPIO.output(4, GPIO.HIGH)

def motorUp():
	GPIO.output(7, GPIO.LOW)
	sleep(measurement * passesNumber)	# change this for the real world too
	GPIO.output(7, GPIO.HIGH)
    
def motorDown():
	GPIO.output(15, GPIO.LOW)
	sleep(measurement * 1) 			# change this for physical world 
	GPIO.output(15, GPIO.HIGH)
    
def sawAway():
	GPIO.output(18, GPIO.LOW)
	sleep(motionTime)
	GPIO.output(18, GPIO.HIGH)

def sawTowards():
	GPIO.output(22, GPIO.LOW)
	sleep(motionTime)
	GPIO.output(22, GPIO.HIGH)

# PROGRAM STARTS BELOW!
while True:

	print("Welcome to sawOS v0.1. This program is provided with ABSOLUTELY NO WARRANTY and is used at your own risk")

	while begin == 0:
		sleep(1) 
		howMuchToCut()
		travelTime()
		passes()
		ynQuery()

	for x in range(0, passesNumber):
		pumpOn()
		motorDown()
		sawAway()
		motorDown()
		sawTowards()

	pumpOff()
	motorUp()
	print("Cut complete\n")
	sleep(3)
	
	measurement = "blank"
	motionTime = "blank"
	passesNumber = 0
	begin = 0

