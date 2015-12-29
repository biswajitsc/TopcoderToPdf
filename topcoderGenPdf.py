import pdfkit
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString
import re
import urllib2
import time
import os

curr = 0
done = 620

filelist = os.listdir('htmls')
# filelist = ['Single Round Match 625 Round 1 - Division I, Level Two']

failed = 0

for filename in filelist:

	if done >= curr:
		curr += 1
		continue

	print "Printing", curr, filename
	parse_fail = False

	try:
		parse = bs(open('./htmls/'+filename))
		# parse = bs(open(filename))

		[obj.extract() for obj in parse.findAll(width = "180")]

		node = parse.find_all('span', 'bodySubhead')[0]
		node.string = unicode('\n  '+filename+'\n')

		parse = parse.prettify(formatter = 'normal')

		out = open('./proc_htmls/{0}'.format(filename), 'w')
		out.write(parse)
		out.close()
	except:
		failed += 1
		parse_fail = True

	options = {
	    'page-size': 'A5',
	    'margin-top': '0.30in',
	    'margin-right': '0.0in',
	    'margin-bottom': '0.30in',
	    'margin-left': '0.0in',
	    'cache-dir': 'html_cache',
	    # 'proxy': '10.3.100.207:8080'
	}

	if not parse_fail:
		pdfkit.from_file(open('./proc_htmls/{0}'.format(filename)), './PDFs/{0}.pdf'.format(filename), options = options)
	else:
		print "File does not exist"

	print "Failed", failed
	curr += 1

	time.sleep(1)

	# break
