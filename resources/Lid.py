import RPi.GPIO as GPIO
from time import sleep

class Lid:
    inputPin1 = 17      #in1
    inputPin2 = 27      #in2
    powerLevelPin = 7   #encle
    motorSpeed = GPIO.PWM
    lidIsOpen = False

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.inputPin1, GPIO.OUT)
        GPIO.setup(self.inputPin2, GPIO.OUT)
        GPIO.setup(self.powerLevelPin, GPIO.OUT)
        GPIO.output(self.inputPin1, GPIO.LOW)
        GPIO.output(self.inputPin2, GPIO.LOW)
        self.motorSpeed = GPIO.PWM(self.powerLevelPin,1000)
        self.motorSpeed.start(0)


    def openLid(self):
        #if not lidIsOpen:
        print("openning lid")
        self.open(100)
        sleep(1)
        self.turn_off()
        print("finished openning lid")
            #lidIsOpen = True

    def closeLid(self):
        #if lidIsOpen:
        print("closing lid")
        self.close(100)
        sleep(0.5)
        self.turn_off()
        print("finished closing lid")
            #lidIsOpen = False


    def turn_off(self):
        GPIO.output(self.inputPin1,GPIO.LOW)
        GPIO.output(self.inputPin2,GPIO.LOW)

    def open(self, speed):
        self.motorSpeed.ChangeDutyCycle(speed)
        GPIO.output(self.inputPin1,GPIO.LOW)
        GPIO.output(self.inputPin2,GPIO.HIGH)

    def close(self, speed):
        self.motorSpeed.ChangeDutyCycle(speed)
        GPIO.output(self.inputPin1,GPIO.HIGH)
        GPIO.output(self.inputPin2,GPIO.LOW)
