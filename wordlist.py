from api import youdao
import os

class wordlist():
	'''
	name
	wordlist = {'word':'audioPath'}
	'''
	def __init__(self, name, type=0):
		self._listName = name  # 单词表名
		self._wordlist = {} # 默认：字典为空
		#关于worlist()初始化：
		#不能通过wordlist={}作为输入参量，初始化
		self._wordnum = len(self._wordlist)
		#print("Initialized...wordnum:%d" % self._wordnum)
		self._type = type # 默认：美音
		self.yd = youdao(type)
		self._dirSpeech = self.yd._dirSpeech # 音频文件存放dir地址
		
	def add(self, word=''):
		word = word.lower()
		if not word:  #or '' == word
			print('添加失败，当前输入为空');
		else:
			audioPath = self.yd.dl(word)
			if audioPath != -1:
				self._audioPath = audioPath # 下载音频，返回音频地址
				self._wordlist[word] = self._audioPath  # 添加word
				self._wordnum += 1
				print('%s添加成功，音频文件地址:%s' % (word, self._wordlist[word]))
			
	def dele(self, word=''):
		word = word.lower()
		if not word:  #by default
			del_word = self._wordlist.popitem()[0] #remove the last item
		else:
			del_word = word #remove item by key
			self._wordlist.pop(del_word)
		print('%s删除成功' % del_word)
				
				
			
