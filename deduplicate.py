# Data Deduplicator
# Author: Ynl0zq
# https://github.com/bytrix
# 
# if data in data.txt like this:
# a
# a
# b
# b
# will generate data.uniq.txt like this:
# a
# b

import sys
import os

try:
	if sys.argv[1] == '-f':
		fileArgv = sys.argv[2]
		filename = fileArgv
	else:
		print 'Usage: -f filename'
		sys.exit()
except IndexError, e:
	print 'Usage: -f filename'
	sys.exit()

try:
	file = open(filename)
	partOne = filename.split('.')[0]
	partTwo = filename.split('.')[1]
	outFilename = partOne + '.uniq.' + partTwo
	if not os.path.exists(outFilename):
		outFile = open(outFilename, 'w')
		output = ""
		data = file.read()
		urls = data.split('\n')
		index = 0
		length = len(urls)

		for i in xrange(0 ,length-1):
			if urls[i] != urls[i+1]:
				index += 1
				# print urls[i]
				output += urls[i]+"\n"

		index += 1
		# print urls[length-1]
		output += urls[length-1]
		# print output
		outFile.write(output)
		outFile.close()
		print 'File ' + outFilename + ' created!'
	else:
		print 'File ' + outFilename + ' already exists!'
except IOError, e:
	print 'File not found!'
