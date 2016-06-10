# hashses are single-line comments, three ''' are multiline comments

from time import sleep # import the sleep function from the time module
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

''' you need to define your various functions up here, e.g.
def motorUp:
    lift table up blah blah'''

measurement = "blank"
motionTime = "blank"
begin = 0

# funtion below will ask for input and check if input is a number
def howMuchToCut():
    global measurement
    measurement = input("Plese enter the measurement you require here: ") # store input in variable "measurement"
    while not measurement.isnumeric(): # while "measurement" is not a number print you did it wrong and get input again
        print(measurement, "is not a valid input")
        measurement = input("Please re-enter your measurement here: ")    
    float(measurement) # convert what you entered to a floating point number (a decimal)
    print("You have entered:",measurement) # print the value you entered 

def travelTime():
    global motionTime
    motionTime = input("Please enter traveltime in seconds")
    while not motionTime.isnumeric():
        print(motionTime, "in not a valid input")
        motionTime = input("Please re-enter your travel time here: ")
    int(motionTime)
    print("You have entered ", motionTime)
        

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
    sleep(5)
    GPIO.output(10, False)

def sawTowards():
    GPIO.output(11, True)
    sleep(5)
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

for passes
pumpOn()
motorDown()
sawAway()
motorDown()
sawTowards()


















