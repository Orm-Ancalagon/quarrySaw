# hashses are single-line comments, three ''' are multiline comments

from time import sleep # import the sleep function from the time module
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

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

def motorUp():
	GPIO.output(17, True)
	sleep(10)
	GPIO.output(17, False)
	GPIO.cleanup()
    
def motorDown():
	GPIO.output(27, True)
	sleep(measurement * 1) # change this for physical world 
	GPIO.output(27, False)
    
def sawAway():      #this time needs to correspond travel time 
	GPIO.output(10, True)
	sleep(travelTime)
	GPIO.output(10, False)

def sawTowards():
	GPIO.output(11, True)
	sleep(traveTime)
	GPIO.output(11, False)

def pumpOn():
	GPIO.output(8, True)

def pumpOff():
	GPIO.output(8, False)

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


















