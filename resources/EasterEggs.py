from Scale import Scale
from Lid import Lid
from Speaker import Speaker
from time import sleep

class KobeBryant:
	@staticmethod
	def play():
		path = 'Recordings/KobeMode/'
		scale = Scale()
		lid = Lid()
		oldWeight =scale.getWeight()
		lid.openLid()
		Speaker.playSound(path + 'buzzer.mp3')
		lid.closeLid()

		if scale.getWeight() >oldWeight:
			Speaker.playSound('cheering.mp3')
		else:
			Speaker.fullTrash()

class Halloween:
	@staticmethod
	def play():
		path = 'Recordings/KobeMode/'
		scale = Scale()
		lid = Lid()
		oldWeight =scale.getWeight()
		lid.openLid()
		Speaker.playSound(path + 'buzzer.m4a')
		lid.closeLid()

		if scale.getWeight() >oldWeight:
			Speaker.playSound('cheering.mp3')
		else:
			Speaker.fullTrash()

class Music:
	@staticmethod
	def play():
		os.system('mpg123 http://ice1.somafm.com/u80s-128-mp3')

class System:
	@staticmethod
	def reboot():
		os.system('sudo reboot')
