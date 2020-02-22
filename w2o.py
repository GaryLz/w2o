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
	最后生成wordlist_audio.mp3
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
		
	def dele(self, word):
		self._wl.dele(word)
	
	def printwl(self):
		"""
		print wordlist to console
		"""
		loop = 1
		for word in self._wl._wordlist.keys():
			print('%d.%s' %(loop, word))
			loop += 1
			
	def wri2txt(self):
		"""
		写入txt,记录wordlist
		"""
		fileName = self._wl._listName + '.txt'
		txtFile = open(fileName, 'w')
		loop = 1
		for word in self._wl._wordlist.keys():
			txtFile.write(str(loop)+ '. ' + word)
			txtFile.write('\n')
			loop += 1
		txtFile.close()
		print("写入txt文件成功,%s" % fileName)	
						
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
	while True:
		#print(os.getcwd())
		print("======here is w2o program=====")		
		print("1. by console manually")
		print("2. from .txt file")
		print("0. exit")			
		print("==============================")
		chosen = input("select:")
		#os.system('clear')
		if chosen == '1':
			byConsole()
			
		elif chosen == '2':
			generatefrmtxt()
			
		elif chosen == '0':
			return None
		else:
			print('input_error')			
		print("\n")
		
def byConsole():
	"""
	generate a wordlist manually on console:
		type '#' to end
	""" 
	name = input("wordlist-name:\n")
	wl = w2o(name)
	#os.system('clear')
	print("any word? If not, pleast type # to exit")
	while True:
		wl.printwl()
		word = input()
		if '#' == word:
			break
		elif '-' == word[0]:
			wl.dele(word[1:])
		else:
			wl.add(word)
	#os.system('clear')
	print("next follows write2txt, write2json, merge2mp3 Funcs:")
	wl.wri2txt()
	wl.wri2json()
	wl.merge2mp3()
	os.chdir('..') # back to the previous dir
	print("单词表{}生成成功".format(wl._wl._listName))
		
def generatefrmtxt():
	"""
	from .txt file 
	generate audio files.
	Rules:
		1. # wordlist_name: for file_name
		2. each word for one line
		3. type '#' to end in the last line
	"""
	# 判断当前cwd是否在cwd,防止两种模式交替使用报错（不同cwds）
	base = os.path.basename(os.getcwd())
	if base != 'w2o':
		os.chdir('../w2o')
	with open("./wordlist_input.txt", 'r', encoding = 'UTF-8') as f:
		lines = f.readlines()
	f.close()
	success = [] #记录-成功生成的wordlist_names
	for line in lines:
		striped = line.strip() #去除字串符头尾特殊符号
		#print(repr(striped))
		if striped == '':
			#'newline'
			continue
		elif striped[0] == '#':
			if len(striped) > 1:
				#'title'
				name = striped[2:].replace(' ', '-')
				wl = w2o(name)
			else:
				#'endline'
				wl.wri2txt()
				wl.wri2json()
				wl.merge2mp3()
				success.append(wl._wl._listName)
				os.chdir('..') # back to the previous dir
		else:
			#'word'
			word = striped
			wl.add(word)
		
	print("共有{}个wordlists生成成功: {} ".format(len(success), success))
						
if __name__ == "__main__":
	main()