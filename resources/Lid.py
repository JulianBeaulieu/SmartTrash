import RPi.GPIO as GPIO
from time import sleep

class Lid:
    inputPin1 = 17      #in1
    inputPin2 = 27      #in2
    powerLevelPin = 7   #encle
    motorSpeed = GPIO.PWM
    #lidIsOpen = False

    def __init__(self):
        #self.dontCloseYet = True
        self.lidIsOpen = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.inputPin1, GPIO.OUT)
        GPIO.setup(self.inputPin2, GPIO.OUT)
        GPIO.setup(self.powerLevelPin, GPIO.OUT)
        GPIO.output(self.inputPin1, GPIO.LOW)
        GPIO.output(self.inputPin2, GPIO.LOW)
        self.motorSpeed = GPIO.PWM(self.powerLevelPin,1000)
        self.motorSpeed.ChangeDutyCycle(100)
        self.motorSpeed.start(0)


    def openLid(self):
        #self.dontCloseYet = False
        if not self.lidIsOpen:
        	print("openning lid")
	        self.open()
	        sleep(2)
	        self.turn_off()
	        print("finished openning lid")
	        self.lidIsOpen = True
        #sleep(2)
        #self.dontCloseYet = True


    def closeLid(self):
        if self.lidIsOpen:
        	print("closing lid")
	        self.close()
	        sleep(2)
	        self.turn_off()
	        print("finished closing lid")
	        self.lidIsOpen = False


    def turn_off(self):
        GPIO.output(self.inputPin1,GPIO.LOW)
        GPIO.output(self.inputPin2,GPIO.LOW)

    def close(self):
        GPIO.output(self.inputPin1,GPIO.LOW)
        GPIO.output(self.inputPin2,GPIO.HIGH)

    def open(self):
        GPIO.output(self.inputPin1,GPIO.HIGH)
        GPIO.output(self.inputPin2,GPIO.LOW)
