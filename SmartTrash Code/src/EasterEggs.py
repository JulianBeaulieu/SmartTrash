from Scale import Scale
from Lid import Lid
from Speaker import Speaker
from time import sleep
from time import ctime
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

class HalloweenThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print "Starting " + self.name
		# Get lock to synchronize threads
		threadLock.acquire()
		print_time(self.name, self.counter, 3)
		# Free lock to release next thread
		threadLock.release()

	def print_time(threadName, delay, counter):
		while counter:
			time.sleep(delay)
			print "%s: %s" % (threadName, time.ctime(time.time()))
			counter -= 1


class Halloween:
	@staticmethod
	def play(lid):
		# Create new threads
		thread1 = HalloweenThread(1, "Thread-1", 1)
		thread2 = HalloweenThread(2, "Thread-2", 2)

		# Start new Threads
		thread1.start()
		thread2.start()

		# Add threads to thread list
		threads.append(thread1)
		threads.append(thread2)

		# Wait for all threads to complete
		for t in threads:
		    t.join()
		print "Exiting Main Thread"


class Music:
	@staticmethod
	def play():
		os.system('mpg123 http://ice1.somafm.com/u80s-128-mp3')

class System:
	@staticmethod
	def reboot():
		os.system('sudo reboot')
