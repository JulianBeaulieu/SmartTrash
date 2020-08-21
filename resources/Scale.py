import RPi.GPIO as GPIO
from hx711 import HX711
from Speaker import Speaker

class Scale:
	def __init__(self):
		self.hx =HX711(24, 23)
		self.hx.set_reading_format("MSB", "MSB")
		self.hx.set_reference_unit(255) # unit needs updating
		self.hx.reset()
		self.hx.tare()
		self.limit = 1500	# trash limit

	def checkWeight(self):	#execute after closing
		if self.getWeight() >= self.limit:
			print("take out the trash")
			Speaker.trashDay()
			return 0

	def getWeight(self):
		currentWeight =self.hx.get_weight(5)
		self.hx.power_down();
		self.hx.power_up();
		return currentWeight
