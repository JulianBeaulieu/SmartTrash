from time import sleep
import RPi.GPIO as GPIO
from Lid import Lid

class Sensors:
    #PINS
    OPEN_BUTTON = 20
    CLOSE_BUTTON = 21
    BOUNCE_TIME = 2000
    trashCanLid = None

    def __init__(self, newTrashCanLid):
        #sets up the GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.OPEN_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.CLOSE_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        # Makes interrupts that monitor pins to check if button or sensor is being pressed
        GPIO.add_event_detect(self.OPEN_BUTTON, GPIO.BOTH, callback = self.open_button_callback, bouncetime = self.BOUNCE_TIME)
        GPIO.add_event_detect(self.CLOSE_BUTTON, GPIO.BOTH, callback = self.close_button_callback, bouncetime = self.BOUNCE_TIME)

        self.trashCanLid = newTrashCanLid

    def open_button_callback(self, channel):
        trashCanLid.openLid()

    def close_button_callback(self, channel):
        trashCanLid.closeLid()
