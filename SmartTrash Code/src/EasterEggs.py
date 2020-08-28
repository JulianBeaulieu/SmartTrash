from Scale import Scale
from Lid import Lid
from Speaker import Speaker
from time import sleep
import threading

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
		self.threadID =id
		self.name =name
		self.lid =lid
		self.increased =False
		self.scale =Scale()
		self.weight =self.scale.getWeight()

	def run(self):
		for i in range(10):
			if self.scale.getWeight >self.weight:
				self.increased =True

		closeT = KobeModeLid(self.lid, 0)
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

class Halloween:
	@staticmethod
	def play(lid):

class Music:
	@staticmethod
	def play():
		os.system('mpg123 http://ice1.somafm.com/u80s-128-mp3')

class System:
	@staticmethod
	def reboot():
		os.system('sudo reboot')
