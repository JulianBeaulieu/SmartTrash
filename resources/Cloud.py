#Import the Modules Required
import time
from pubnub import Pubnub

class Cloud:
    # Initialize the Pubnub Keys
    g_pub_key = "pub-c-e172d2c0-f4ff-4cb7-b610-46e2cbce18d5"
    g_sub_key = "sub-c-82bf53a4-bd8a-11ea-a44f-6e05387a1df4"

    '''****************************************************************************************
    Function Name   :   init
    Description     :   Initalize the pubnub keys and Starts Subscribing
    Parameters      :   None
    ****************************************************************************************'''
    def init(self, trashCanLid):
        #Pubnub Initialization
        global pubnub
        pubnub = Pubnub(publish_key=g_pub_key,subscribe_key=g_sub_key)
        pubnub.subscribe(channels='Trash-Client', callback=callback, error=callback, reconnect=reconnect, disconnect=disconnect)

    '''****************************************************************************************
    Function Name   :   alexaControl
    Description     :   Alexa Control, commands received and action performed
    Parameters      :   controlCommand
    ****************************************************************************************'''
    def lidControl(controlCommand):
        if(controlCommand.has_key("trigger")):
            if(controlCommand["trigger"] == "open" and controlCommand["status"] == 1):
                print ("Opening Lid")
            elif(controlCommand["trigger"] == "close" and controlCommand["status"] == 0):
                print ("Closing Lid")
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
