from bs4 import BeautifulSoup
import re
import urllib2
import time

def isname(tag):
	if not tag.has_attr('href'):
		return False

	if re.search("/tc\?module=ProblemDetail&rd=[0-9]*&pm=[0-9]*", tag['href']):
		return True
	else:
		return False

def getname(file):
	# return file.find(text = re.compile("Single Round Match*"))
	return file.find(isname).string

def getproblemlist():
	file = open("TopCoder Statistics - Problem Archive.html", "r")
	res = re.findall('http://community.topcoder.com/stat\?c=problem_statement&pm=[0-9]*', ""+file.read())
	return res

def getproblem(urlname):
	print "Getting", urlname

	# input = open("temp.html", "r")
	input = urllib2.urlopen(urlname)
	parse = BeautifulSoup(input)
	input.close()

	# Remove leftNavWrapper
	[obj.extract() for obj in parse.findAll("div", "leftNavWrapper")]

	# Remove Header
	[obj.extract() for obj in parse.findAll("header")]

	# Remove Footer
	[obj.extract() for obj in parse.findAll("footer")]

	# Remove Scripts
	# [obj.extract() for obj in parse.findAll("script")]

	name = getname(parse)
	print name, "\n"

	parse = parse.prettify(formatter = "minimal")
	output = open("htmls/"+name, "w")
	output.write(parse)
	output.close()

problems = getproblemlist()
print len(problems), "Problems"
cnt = 1
done = 0

for file in problems:
	print cnt, ": ",
	
	if cnt > done:
		try:
			getproblem(file)
			time.sleep(2)
		except:
			print "Cannot get problem"
	else:
		print

	cnt += 1
	# if cnt > 44:
	# 	break
