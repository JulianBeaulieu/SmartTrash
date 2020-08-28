from Scale import Scale
from Lid import Lid
from Speaker import Speaker
from time import sleep
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
	def __init__(self, threadID, lid):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.lid = lid

	def run(self):
		print "Starting Lid Movement"

		self.lid.openLid()
		self.lid.closeLid()

		print "Ending Lid Movement"

class HalloweenScreamThread (threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID

	def run(self):
		print "Starting Screaming"

		Speaker.playSound('../Recordings/HalloweenMode/scream.mp3')
		Speaker.playSound('../Recordings/HalloweenMode/scream.mp3')

		print "Ending Screaming"

class Halloween:
	@staticmethod
	def play(lid):
		# Create new threads
		thread1 = HalloweenLidMovementThread(1, lid)
		thread2 = HalloweenScreamThread(2)

		# Start new Threads
		thread1.start()
		thread2.start()

		# Add threads to thread list
		#threads.append(thread1)
		#threads.append(thread2)

		# Wait for all threads to complete
		#for t in threads:
		#    t.join()
		#print "Exiting Main Thread"


class Music:
	@staticmethod
	def play():
		os.system('mpg123 http://ice1.somafm.com/u80s-128-mp3')

class System:
	@staticmethod
	def reboot():
		os.system('sudo reboot')
