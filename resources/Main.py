#!/usr/bin/env python3
import signal
import sys
from time import sleep
import RPi.GPIO as GPIO
import time
from pubnub import Pubnub

inputPin1 = 17      #in1
inputPin2 = 27      #in2
powerLevelPin = 7   #encle
motorSpeed = GPIO.PWM
lidIsOpen = False
#PINS
OPEN_BUTTON = 20
CLOSE_BUTTON = 21
BOUNCE_TIME = 2000

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(inputPin1, GPIO.OUT)
GPIO.setup(inputPin2, GPIO.OUT)
GPIO.setup(powerLevelPin, GPIO.OUT)
GPIO.output(inputPin1, GPIO.LOW)
GPIO.output(inputPin2, GPIO.LOW)
motorSpeed = GPIO.PWM(powerLevelPin,1000)
motorSpeed.start(0)
#sets up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(OPEN_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(CLOSE_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Makes interrupts that monitor pins to check if button or sensor is being pressed
GPIO.add_event_detect(OPEN_BUTTON, GPIO.BOTH, callback = open_button_callback, bouncetime = BOUNCE_TIME)
GPIO.add_event_detect(CLOSE_BUTTON, GPIO.BOTH, callback = close_button_callback, bouncetime = BOUNCE_TIME)


def openLid(self):
    if not lidIsOpen:
        print("openning lid")
        open(100)
        sleep(0.5)
        turn_off()
        print("finished openning lid")
        lidIsOpen = True

def closeLid(self):
    if lidIsOpen:
        print("closing lid")
        close(100)
        sleep(0.5)
        turn_off()
        print("finished closing lid")
        lidIsOpen = False


def turn_off(self):
    GPIO.output(inputPin1,GPIO.LOW)
    GPIO.output(inputPin2,GPIO.LOW)

def open(self, speed):
    motorSpeed.ChangeDutyCycle(speed)
    GPIO.output(inputPin1,GPIO.LOW)
    GPIO.output(inputPin2,GPIO.HIGH)

def close(self, speed):
    motorSpeed.ChangeDutyCycle(speed)
    GPIO.output(inputPin1,GPIO.HIGH)
    GPIO.output(inputPin2,GPIO.LOW)

def open_button_callback(self, channel):
    trashCanLid.openLid()

def close_button_callback(self, channel):
    trashCanLid.closeLid()


# Initialize the Pubnub Keys
g_pub_key = "pub-c-e172d2c0-f4ff-4cb7-b610-46e2cbce18d5"
g_sub_key = "sub-c-82bf53a4-bd8a-11ea-a44f-6e05387a1df4"
trashCanLid = None

'''****************************************************************************************
Function Name   :   init
Description     :   Initalize the pubnub keys and Starts Subscribing
Parameters      :   None
****************************************************************************************'''

    #Pubnub Initialization
    global pubnub
    pubnub = Pubnub(publish_key = g_pub_key, subscribe_key = g_sub_key)
    pubnub.subscribe(channels = 'Trash-Client', callback = callback, error = callback, reconnect = reconnect, disconnect = disconnect)

    trashCanLid = newTrashCanLid

'''****************************************************************************************
Function Name   :   alexaControl
Description     :   Alexa Control, commands received and action performed
Parameters      :   controlCommand
****************************************************************************************'''
def lidControl(controlCommand):
    if(controlCommand.has_key("trigger")):
        if(controlCommand["trigger"] == "open" and controlCommand["status"] == 1):
            trashCanLid.openLid()
        elif(controlCommand["trigger"] == "close" and controlCommand["status"] == 0):
            trashCanLid.closeLid()
        else:
            print("OOPS something went wrong")
    else:
        pass


'''****************************************************************************************
Function Name   :   callback
Description     :   Waits for the message from the alexaTrigger channel
Parameters      :   message - Sensor Status sent from the hardware
                    channel - channel for the callback
****************************************************************************************'''
def callback(message, channel):
    if(message.has_key("requester")):
        lidControl(message)
    else:
        pass

'''****************************************************************************************
Function Name   :   error
Description     :   If error in the channel, prints the error
Parameters      :   message - error message
****************************************************************************************'''
def error(message):
    print("ERROR : " + str(message))

'''****************************************************************************************
Function Name   :   reconnect
Description     :   Responds if server connects with pubnub
Parameters      :   message
****************************************************************************************'''
def reconnect(message):
    print("RECONNECTED")

'''****************************************************************************************
Function Name   :   disconnect
Description     :   Responds if server disconnects from pubnub
Parameters      :   message
****************************************************************************************'''
def disconnect(message):
    print("DISCONNECTED")


#This method let's the user ctrl-c out of the program
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

if __name__ == '__main__':

    #Makes sure you can exit the program
    signal.signal(signal.SIGINT, signal_handler)

    i = 0
    while True:
        #do nothing
        print "Off"
        sleep(0.2)
