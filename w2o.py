from wordlist import wordlist
from pydub import AudioSegment
from json_formatter import JsonFormatter
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
		#print(os.getcwd())
		
	def add(self, word):
		self._wl.add(word)
	
	def checkwl(self):
		loop = 1
		for word in self._wl._wordlist.keys():
			print('%d.%s' %(loop, word))
			loop += 1
			
	def wri2json(self):
		jsnObject = json.dumps(self._wl._wordlist)
		fileName = self._wl._listName + '.json'
		newFile = open(fileName, 'w')
		newFile.writelines(jsnObject)
		print("写入json文件成功,%s" % fileName)
		newFile.close()
		JsonFormatter(name=fileName).render()
		
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
		exportPath = os.getcwd()+os.sep+self._wl._listName+'.mp3'
		mp3_merged.export(exportPath, format='mp3')
		print("合并mp3成功，所在地址%s" % exportPath)	
	
		
def main():
	print("======here is w2o program=====")		
	print("1. new a wordlist ")
	print("0. exit")			
	print("==============================")
	chosen = input("select:")
	os.system('clear')
	if chosen == '1':
		name = input("wordlist-name:\n")
		wl = w2o(name)
		os.system('clear')
		print("any word? If not, pleast type # to exit")
		while True:
			wl.checkwl()
			word = input()
			if '#' == word:
				break
			wl.add(word)
		os.system('clear')
		print("next follows write2json, merge2mp3 Func...")
		wl.wri2json()
		wl.merge2mp3()
		main()
	elif chosen == '0':
		return None
	else:
		print('input_error')			
				
if __name__ == "__main__":
	main()