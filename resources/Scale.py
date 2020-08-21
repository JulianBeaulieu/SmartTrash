import RPi.GPIO as GPIO
from hx711 import HX711

class Scale:
	def __init__(self):
		self.hx =HX711(5,6)
		self.hx.set_reading_format("MSB", "MSB")
		self.hx.set_reference_unit(0) # unit needs updating
		self.hx.reset()
		self.hx.tare()
		self.limit =5	# trash limit

	def checkWeight(self):	#execute after closing
		if self.getWeight >= self.limit:
			#send recording to speaker
			return 0

	def getWeight(self):
		currentWeight =self.hx.get_weight(5)
		self.hx.power_down();
		self.hx.power_up();
		return currentWeight
