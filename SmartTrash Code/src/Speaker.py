import os
import sys
import random
from Language import Language

class Speaker:
	@staticmethod
	def fullTrash():
		language = Langauge()
		path ='Recordings/FullTrash/' + language.getLanguage() + '/'
		file = str(random.choice(os.listdir(path)))
		os.system('mpg123 ' + path + file)

	@staticmethod
	def trashDay():
		language = Langauge()
		path ='Recordings/TrashDay/' + language.getLanguage() + '/'
		file = str(random.choice(os.listdir(path)))
		os.system('mpg123 ' + path + file)

	@staticmethod
	def playSound(path):
		os.system('mpg123 ' + path)
