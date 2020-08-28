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

'''
class KobeBryant:
	@staticmethod
	def play(lid):
		path = '../Recordings/KobeMode/'
		scaleT = KobeModeScaleThread(1, 'scale', lid)
		buzzerT = KobeModeSound(2, 'cheer', path + 'buzzer.mp3')
		openT = KobeModeLid(lid, 1)

		scaleT.start()
		buzzerT.start()
		openT.start()

class KobeModeScaleThread(threading.Thread):
	def __init__(self, id, name, lid):
		threading.Thread.__init__(self)
		self.threadID = id
		self.name = name
		self.lid = lid
		self.increased = False
		self.scale = Scale()
		self.weight = self.scale.getWeight()

	def run(self):
		for i in range(10):
			if self.scale.getWeight > (self.weight + 4):
				self.increased = True

		closeT = KobeModeLid(self.lid, 0)
		soundT = KobeModeSound(2, 'sound', '../Recordings/KobeMode/cheering.mp3')

		if self.increased:
			soundT = KobeModeSound(2, 'sound', '../Recordings/KobeMode/cheering.mp3')
		else:
			soundT = KobeModeSound(2, 'sound', '../Recordings/KobeMode/boo.mp3')

		closeT.start()
		soundT.start()

class KobeModeLid(threading.Thread):
	def __init__(self, lid, s):
		threading.Thread.__init__(self)
		self.lid =lid
		self.status =s

	def run(self):
		if self.status:
			self.lid.openLid()
		else:
			self.lid.closeLid()

class KobeModeSound(threading.Thread):
	def __init__(self, id, name, path):
		threading.Thread.__init__(self)
		self.threadID =id
		self.name =name
		self.path =path

	def run(self):
		Speaker.playSound(self.path)
'''

class KobeBryant:
	@staticmethod
	def play(lid):
		path = '../Recordings/KobeMode/'
		scaleThread = KobeModeScaleThread(1)
		lidThread = KobeModeLid(1, lid)

		scaleThread.start()
		lidThread.start()

class KobeModeScaleThread(threading.Thread):
	def __init__(self, id):
		threading.Thread.__init__(self)
		self.threadID = id
		self.increased = False
		self.scale = Scale()
		self.weight = self.scale.getWeight()

	def run(self):
		for i in range(30):
			#50, 150 too low
			if self.scale.getWeight > (self.weight + 400):
				print(str(self.scale.getWeight))
				self.increased = True
			sleep(0.1)

		if self.increased:
			Speaker.playSound('../Recordings/KobeMode/cheering.mp3')
		else:
			Speaker.playSound('../Recordings/KobeMode/boo.mp3')

class KobeModeLid(threading.Thread):
	def __init__(self, id, lid):
		threading.Thread.__init__(self)
		self.threadID = id
		self.lid =lid

	def run(self):
		self.lid.openLid()
		sleep(2)
		self.lid.closeLid()












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
			for i in range(3):
				self.lid.open()
				sleep(.3)
				for i in range(10):
					self.lid.close()
					sleep(.1)
					self.lid.open()
					sleep(.1)
				self.lid.close()
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
