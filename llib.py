########################_OUT_######################

#____character output. 
def extPrint(text,delay = 0.2):
	import time,sys
	text = text+"\n"
	for i in text:
		time.sleep(delay)
		sys.stdout.write(i)
		sys.stdout.flush()
	return text
#____wrapper for out
def logger(text):
	from sys import platform,stdout
	splitter = '\n###=============================###\n'
	stdout.write(splitter+'#~'+platform+'_logMsg: '+text+splitter)

###########################_JSON_####################
#___open and load json in python
def jsonOpen(filename):
	import json
	with open(filename,"r",encoding = 'UTF-8') as file:
		f = json.load(file)
	return f
#___dump json and save to file
def jsonSave(data,filename,indent = 4):
	import json
	try:
		with open(filename,"w",encoding ='UTF-8')  as file:
			json.dump(data,file,ensure_ascii=False,indent = indent)
		return True
	except Exception:
		return False

##########################_FILES_###################
#___save data to file. mode is "w","wb","a"
def saveToFile(data,filename,mode = "w"):
	with open(filename, mode,encoding = "UTF-8") as file:
		file.write(data+'\n')
		file.close
	return data
#__open file to list(or string if args[0] = s)
def openFile(filename,mode = "r",*args):
	try:
		if args[0] == 'r':
			with open(filename,mode,encoding = "UTF-8") as file:
				data = file.read()
				dataList = data.split("\n")
				return dataList
		elif args[0] == 'l':
			with open(filename,mode,encoding = "UTF-8") as file:
				data = file.read()
				dataList = data.split(args[1])
				return dataList
		elif args[0] == 's':
			with open(filename,mode,encoding = "UTF-8") as file:
				data = file.read()
				return data
	except Exception:
		with open(filename,mode,encoding = "UTF-8") as file:
			data = file.read()
			dataList = data.split("\n")
			return dataList
#__download file from src to filename
def download(src,filename):
	try:
		try:
			import urllib.request as url
		except:
			install("request")
			import urllib.request as url
		res = url.urlretrieve(src,filename)
		return True
	except:
		return False


#########################_CROSSPLATFORM_FUNC_################
#___clear console window
def cClear():
	import subprocess
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['clear'],shell = True)
		return True
	elif platform == 'win32':
		subprocess.call(['cls'],shell = True)
		return True
	elif platform == "darwin":
		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
		return True
	else:
		logger('Unknow system :(')
		return False
#___make directory to path
def makeDir(path):
	import subprocess, os
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['mkdir '+path],shell = True)
		return True
	elif platform == 'win32':
		os.mkdir(path)
		return True
#	elif platform == "darwin":
#		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
	else:
		logger('Unknow system :(')
		return False
#___remove file or directory to path
def remove(path):
	import subprocess, os
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['rm -rf '+path],shell = True)
		return True
	elif platform == 'win32':
		try:
			os.rmdir(path)
			return True
		except:
			os.remove(path)
			return True
#	elif platform == "darwin":
#		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
	else:
		logger('Unknow system :(')
		return False
#___copy file from path to toPath
def copy(path,toPath):
	import subprocess, os
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['cp -r'+path+' '+toPath+'/'+path],shell = True)
		return True
	elif platform == 'win32':
		subprocess.call(['copy /Y'+path+' '+toPath+'/'+path],shell = True)
		return True
#	elif platform == "darwin":
#		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
	else:
		logger('Unknow system :(')
		return False
#___copy data in clipboard
def clipCopy(data):
	try:
		import pyperclip
	except:
		install("pyperclip")
		import pyperclip
	try:
		pyperclip.copy(data)
		return True
	except:
		logger('Clipboard error :(')
		return False
#___paste data from clipboard (return data or None)
def clipPaste():
	try:
		import pyperclip
	except:
		install("pyperclip")
		import pyperclip
	try:
		return pyperclip.paste()
	except:
		logger('Clipboard error :(')
		return None
#___install modules.
def install(*modulesNames):
	import subprocess
	listM = ''
	for module in modulesNames:
		try:
			subprocess.call(['pip','install',module])
		except:
			subprocess.call(['pip3','install',module])
		listM += (module+', ')
	cClear()
	return listM+'- successfully installed'
#___generate random symbols 
def randomGen(lenght = 12):
	import random
	alp = "qwertyuiopasdfghjklzxcvbnm"
	rText = ""
	for i in range(int(lenght)):
		k = random.randint(0,len(alp)-1)
		if random.randint(0,1)==1:
			if random.randint(0,1) == 1:
				rText+=alp[k:k+1].upper()
			else:
				rText+=alp[k:k+1]
		else:
			rText+=str(random.randint(0,9))
	return str(rText)
