from Scale import Scale
from Lid import Lid
from Speaker import Speaker
from time import sleep

class KobeBryant:
	@staticmethod
	def play():
		scale = Scale()
		lid = Lid()
		oldWeight =scale.getWeight()
		lid.openLid()
		Speaker.playSound('path to buzzer sound)
		sleep(10)

		if scale.getWeight() >oldWeight:
			Speaker.playSound('path to cheering')
		else:
			Speaker.playSound('path to boo')

		lid.closeLid()
