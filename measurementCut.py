# hashses are single-line comments, three ''' are multiline comments

from time import sleep # import the sleep function from the time module
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)		# pump
GPIO.setup(7, GPIO.OUT)		# motorUp
GPIO.setup(15, GPIO.OUT)	# motorDown
GPIO.setup(18, GPIO.OUT)	# sawAway
GPIO.setup(22, GPIO.OUT)	# sawTowards

measurement = "blank"
motionTime = "blank"
passesNumber = 0
begin = 0

# funtion below will ask for input and check if input is a number
def howMuchToCut():
	while True:
		try:
			global measurement
			measurement = input("Please enter your measurement here")
			measurement = float(measurement)
		except ValueError:
			print("Invalid entry, please enter a number")
			continue
		else:
			print("You have entered:", measurement)
			break    

def travelTime():
	while True:
		try:
			global motionTime
			motionTime = input("Please enter traveltime in seconds")
			motionTime = float(motionTime)
		except ValueError:
			print(motionTime, "is not a valid input, please re-enter")
			continue
		else:
			print("You have entered:", motionTime)
			break

def passes():
	while True:
                try:
                        global passesNumber
                        passesNumber = input("Please enter traveltime in seconds")
                        passesNumber = float(passesNumber)
                except ValueError:
                        print(passesNumber, "is not a valid number of passes, please re-enter")
                        continue
                else:
                        print("You have entered:", passesNumber)
                        break

# function below will ask if you want to proceed
def ynQuery():
	start = input("Do you wish to begin cutting? (y/n)")
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
	GPIO.output(4, True)

def pumpOff():
	GPIO.output(4, False)

def motorUp():
	GPIO.output(7, True)
	sleep(10)	# change this for the real world too
	GPIO.output(7, False)
	GPIO.cleanup()
    
def motorDown():
	GPIO.output(15, True)
	sleep(measurement * 1) # change this for physical world 
	GPIO.output(15, False)
    
def sawAway():      #this time needs to correspond travel time 
	GPIO.output(18, True)
	sleep(travelTime)
	GPIO.output(18, False)

def sawTowards():
	GPIO.output(22, True)
	sleep(traveTime)
	GPIO.output(22, False)

# PROGRAM STARTS BELOW!
print("Welcome to sawOS v0.1. This program is provided with ABSOLUTELY NO WARRANTY and is used at your own risk")

while begin == 0:
	sleep(1) # wait for 1 second
	howMuchToCut()
	travelTime()
	ynQuery()

pumpOn()

for x in range(0, passesNumber)
	motorDown()
	sawAway()
	motorDown()
	sawTowards()

pumpOff()
motoUp()
