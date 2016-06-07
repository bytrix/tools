#-*-coding:utf-8-*-
import os
import re

d = {
	'一': '01',
	'二': '02',
	'三': '03',
	'四': '04',
	'五': '05',
	'六': '06',
	'七': '07',
	'八': '08',
	'九': '09',
	'十': '10',
	'十一': '11',
	'十二': '12',
	'十三': '13',
	'十四': '14',
	'十五': '15',
	'十六': '16',
	'十七': '17',
	'十八': '18',
	'十九': '19',
	'二十': '20',
	'二十一': '21',
	'二十二': '22',
	'二十三': '23',
	'二十四': '24',
	'二十五': '25',
	'二十六': '26',
	'二十七': '27',
	'二十八': '28',
	'二十九': '29',
	'三十': '30',
	'三十一': '31',
	'三十二': '32',
	'三十三': '33',
	'三十四': '34',
	'三十五': '35',
	'三十六': '36',
	'三十七': '37',
	'三十八': '38',
	'三十九': '39',
}

reg = r'\xb5\xda(.*?)\xbc\xaf'	# 第xx集，提取字符xx
fileReg = re.compile(reg)
filesDic = {}
for directories in os.walk('.'):
	for files in directories:
		# print files
		for file in files:
			m = re.findall(reg, file)
			if len(m) == 1:
				# pass
				ch = m[0]
				p = {}
				utf8Ch = ch.decode('gbk').encode('utf8')
				# print d[utf8Ch], file
				index = d[utf8Ch]
				filesDic[index] = file

# for i in filesDic:
	# print i, filesDic[i]

filesDic2 = sorted(filesDic.iteritems(), key = lambda asd:asd[0])

# print '-'*100

for k, v in filesDic2:
	# print k, v
	print v