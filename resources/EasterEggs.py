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

