#!/usr/bin/env python

import fileinput
from os import listdir
import sys
import glob

years = range(0, 1985)
#years = range(1984, 1985)

# can't even deal right now
# 1951 deleted
# 1953 deleted

for xyear in years:

	year = './OpenSubtitles2013/%d' % xyear

	for movieDir in glob.glob(year + '/*' * 1):
		movieFiles = listdir(movieDir)
		cao = filter(lambda x: x.endswith('.xml'), movieFiles)
		for script in cao:
			text = ""
			f=open(movieDir+'/'+script)
			for line in f.readlines():
		    		text += line

			print movieDir+'/'+script
                

			from lxml import etree
			root = etree.fromstring(text)
			result = ""
			tmp = []
  			check = ""
			for x in root.xpath('//document/s/w'):	
				tmp.append(x)
			#print len(tmp)
			if(len(tmp) > 0):
				check = tmp[0].get("id").split('.')[0]
				for i in range(len(tmp)-1):
					if(tmp[i].get("id").split('.')[0] != check):
						check = tmp[i].get("id").split('.')[0]
						result += '\n'
				
					result += tmp[i].text
					if tmp[i+1] == None: 
						continue
					char = tmp[i+1].text[0]
					if (char >= 'A' and char <='z') or (char >= '0' and char <='9'):
						result += ' '
	        	#result += "\n"
			print result
			with open(movieDir+'/subtitle'+ script.replace(".xml", "") + '.txt', 'w') as g:
				g.write(result.encode('utf-8', 'ignore'))
