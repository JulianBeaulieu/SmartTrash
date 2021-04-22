<img src="images/Smart Trash.jpg" alt="drawing" width="100%"/>
<br>
<br>
Smart Trash® will revolutionize your trash experience. Control it with your Google Home and Alexa devices. It will remind you to take your trash out and help you use it if you are physically not able to. Or you just want a really cool bin to throw paper in like your Micheal Jordan without your dog getting to it. What ever it is that you need, this trash can is the trash can for you.<br><br>


## Parts
1. 3x Raspberry Pi Zero W (We burned 2)
2. Apple power plug (The small square one)
3. Cables for breadboard (A LOT of them)
4. Soldering Iron
5. Loudspeaker
6. 6x Diods (We aren't really experienced in building circuits so we started getting extra just incase)
7. Resistors (just get a lot)
8. Trash can with built in motion sensor
9. Motor controller
10. USB audio dac
13. Perfboard

## Hardware
This took us a long time. We started out by figuring out how the motion sensor
send power to the motor in the housing. Then we came up with a small circuit which
could route the signals to the Raspberry. This is where we burned through two Pis because
we did not fully understand polarity yet and when the circuit board from the trashcan reversed
the polarity the Pi wen't bye bye. Then we figured out how to control the lid motor using the
motor controller. Finally we added The loudspeaker and packaged it up nicely.

<img src="images/power v1.JPG" alt="drawing" width="53%"/>
<img src="images/power v2.JPG" alt="drawing" width="35%"/>
<img src="images/power v3.JPG" alt="drawing" width="30%"/>
<img src="images/final assembly.png" alt="drawing" width="60%"/>
<br><br>

**__Please note that we are NOT professionals, so please DON'T do this at home either.__**

## Software - IoT
We used python to create a script which would listen for messages on PubNub. It would
then run the corresponding command and maybe play some audio. Very straight forward.

## Software - App
The app is very simple and used PubNub to send commands such as change language or
open the lid.

## Smart Assistant
Smart trash was also connected to Google Assistant and Amazon Alexa. Using IFTTT they could
send commands to PubNub which SmartTrash could find and then execute. Unfortunately IFTTT
now costs money and so SmartTrash lost it's Google Assistant and Alexa support.

<!-- <img src="images/lovebox.png" alt="drawing" width="35%"/> -->

## Demo
There is a demo, but I am not going to share that, sorry :D.
