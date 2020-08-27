import os
import sys
import random

class Speaker:
	@staticmethod
	def fullTrash():
		path ='../Recordings/FullTrash/English/'
		file = str(random.choice(os.listdir(path)))
		os.system('mpg123 ' + path + file)

	@staticmethod
	def trashDay():
		path ='../Recordings/TrashDay/English/'
		file = str(random.choice(os.listdir(path)))
		os.system('mpg123 ' + path + file)

	@staticmethod
	def playSound(path):
		os.system('mpg123 ' + path)
