import os
import sys
import random
from Language import Language
from soundplayer import SoundPlayer
from pygame import mixer

class Speaker:
	@staticmethod
	def fullTrash():
		language = Language()
		path ='../Recordings/FullTrash/' + language.getLanguage() + '/'
		file = str(random.choice(os.listdir(path)))
		#os.system('mpg123 ' + path + file)
		p = SoundPlayer(path + file, 2)
		mixer.init()
		sound = mixer.load(path + file)
		sound.play()
		p.play(1)

	@staticmethod
	def trashDay():
		language = Language()
		path ='../Recordings/TrashDay/' + language.getLanguage() + '/'
		file = str(random.choice(os.listdir(path)))
		#os.system('mpg123 ' + path + file)
		p = SoundPlayer(path + file, 2)
		mixer.init()
		sound = mixer.load(path + file)
		sound.play()
		p.play(1)

	@staticmethod
	def playSound(path):
		#os.system('mpg123 ' + path)
		p = SoundPlayer(path, 2)
		mixer.init()
		sound = mixer.load(path)
		sound.play()
		p.play(1)
