from Scale import Scale
from Lid import Lid
from Speaker import Speaker
from time import sleep
import random
import os
import time
import threading

exitFlag = 0
threadLock = threading.Lock()
threads = []

class KobeBryant:
	@staticmethod
	def play(lid):
		path = 'Recordings/KobeMode/'
		scale = Scale()
		oldWeight =scale.getWeight()
		lid.openLid()
		Speaker.playSound(path + 'buzzer.mp3')
		lid.closeLid()

		if scale.getWeight() >oldWeight:
			Speaker.playSound(path + 'cheering.mp3')
		else:
			Speaker.playSound(path + 'boo.mp3')

class HalloweenLidMovementThread (threading.Thread):
	def __init__(self, threadID, lid, filepath):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.lid = lid
		self.file = filepath

	def run(self):
		print "Starting Lid Movement"

		if('scream' in self.file):
			self.lid.openLid()
			self.lid.closeLid()
		else:
			self.lid.open()
			sleep(.3)
			for i in range(30):
				self.lid.close()
				sleep(.1)
				self.lid.open()
				sleep(.2)

			self.lid.close()
			sleep(.3)
			self.lid.turn_off()

		print "Ending Lid Movement"

class HalloweenScreamThread (threading.Thread):
	def __init__(self, threadID, filepath):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.file = filepath

	def run(self):
		print "Starting Screaming"

		Speaker.playSound(self.file)

		print "Ending Screaming"

class Halloween:
	@staticmethod
	def play(lid):
		path = '../Recordings/HalloweenMode/'
		file = str(random.choice(os.listdir(path)))
		# Create new threads
		thread1 = HalloweenLidMovementThread(1, lid, (path + file + ''))
		thread2 = HalloweenScreamThread(2, (path + file + ''))

		# Start new Threads
		thread1.start()
		thread2.start()


class Music:
	@staticmethod
	def play():
		os.system('mpg123 http://ice1.somafm.com/u80s-128-mp3')

class System:
	@staticmethod
	def reboot():
		os.system('sudo reboot')
