import pdfkit
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString
import re
import urllib2
import time
import os

curr = 0
done = -1

filelist = os.listdir('htmls')
# filelist = ['Single Round Match 625 Round 1 - Division I, Level Two']

failed = 0

for filename in filelist:

	if done >= curr:
		curr += 1
		continue

	print "Printing", curr, filename

	try:
		parse = bs(open('./htmls/'+filename))
		# parse = bs(open(filename))

		[obj.extract() for obj in parse.findAll(width = "180")]

		node = parse.find_all('span', 'bodySubhead')[0]
		node.string = unicode('\n  '+filename+'\n')

		# head = parse.find_all('head')
		# head.append(parse.new_tag("link", type="text/css", rel="stylesheet", href="./TopCoder Statistics - Problem Archive_files/coders.css"))
		# head.append(parse.new_tag("link", type="text/css", rel="stylesheet", href="./TopCoder Statistics - Problem Archive_files/login.css"))
		# head.append(parse.new_tag("link", type="text/css", rel="stylesheet", href="./TopCoder Statistics - Problem Archive_files/myHome.css"))
		# head.append(parse.new_tag("link", type="text/css", rel="stylesheet", href="./TopCoder Statistics - Problem Archive_files/newStyles.css"))

		# base = parse.find_all('base')[0]
		# base['href'] = './page_files/'

		# for link in parse.find_all('link')[1:]:
		# 	link['href'] = '.'+link['href']

		# for script in parse.find_all('script', src = True):
		# 	script['src'] = '.'+script['src']

		parse = parse.prettify(formatter = 'normal')

		out = open('./proc_htmls/{0}'.format(filename), 'w')
		out.write(parse)
		out.close()

		# options = {
		#     'page-size': 'A5',
		#     'margin-top': '0.30in',
		#     'margin-right': '0.0in',
		#     'margin-bottom': '0.30in',
		#     'margin-left': '0.0in',
		# }

		# pdfkit.from_string(parse, './PDFs/{0}.pdf'.format(filename), options = options)
	except:
		failed += 1

	print "Failed", failed
	curr += 1

	# time.sleep(2)

	# break