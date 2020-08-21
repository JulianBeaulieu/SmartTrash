import RPi.GPIO as GPIO
from hx711 import HX711

class Scale:
	def __init__(self):
		self.hx =HX711(24, 23)
		self.hx.set_reading_format("MSB", "MSB")
		self.hx.set_reference_unit(415) # unit needs updating
		self.hx.reset()
		self.hx.tare()
		self.limit = 2500	# trash limit

	def checkWeight(self):	#execute after closing
		if self.getWeight() >= self.limit:
			print("take out the trash")
			#send recording to speaker
			return 0

	def getWeight(self):
		currentWeight =self.hx.get_weight(5)
		self.hx.power_down();
		self.hx.power_up();
		return currentWeight
