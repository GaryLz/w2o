from wordlist import wordlist
from pydub import AudioSegment
import os
import json

class w2o():
	"""
	程序思想：
	--操作层--
	根据given name
	生成related wordlist_dir以及audio_dir（API）
	最后生成长wordlist_audio.mp3
	"""
	def __init__(self, name, type=0):
		self._wl = wordlist(name)
		if not os.path.exists(name):
			os.mkdir(name) # 新建wordlist文件夹
		self._curdir = os.path.join(os.curdir, name)
		os.chdir(self._curdir) # cd 到当前wordlist文件夹
		print(os.getcwd())
		
	def add(self, word):
		self._wl.add(word)
	
	def wri2json(self):
		jsnObject = json.dumps(self._wl._wordlist)
		fileName = self._wl._listName + '.json'
		newFile = open(fileName, 'w')
		newFile.write(jsnObject)
		newFile.close()
		
	def merge2mp3(self):
		audio_dir = self._wl._dirSpeech
		gap_between = 1000*3 #间隔3s between rings
		gap_repeat = 1000
		audio_lists = []
		audo_slices = []
		for key in self._wl._wordlist.keys():
			audio_lists.append(key)
		for value in self._wl._wordlist.values():
			audo_slices.append(value)
		sounds = []
		for slice in audo_slices:
			sounds.append(AudioSegment.from_mp3(slice))
		silence_repeat = AudioSegment.silent(gap_repeat)
		silence_between = AudioSegment.silent(gap_between)
		mp3_merged = AudioSegment.empty()
		for sound in sounds:
			mp3_merged += sound+silence_repeat+sound
			mp3_merged += silence_between
			
		mp3_merged.export(os.getcwd()+os.sep+self._wl._listName+'.mp3', format='mp3')
			
		
		
				
	
if __name__ == "__main__":
	tst = w2o('ELC')
	tst.add('good')
	tst.add('sad')
	tst.add('one')
	tst.wri2json()
	tst.merge2mp3()