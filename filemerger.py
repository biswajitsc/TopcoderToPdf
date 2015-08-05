import sys
sys.path.insert(0, './PyPDF2/')

import re
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

def tryint(s):
    try:
        return int(s)
    except:
        if s == 'One':
            return 1
        elif s == 'Two':
            return 2
        elif s == 'Three':
            return 3
        else:
            return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    tem = [ tryint(c) for c in re.split('([0-9]+)|(One)|(Two)|(Three)|(\s)', s) ]
    key = []
    for tok in tem:
        if tok != None and tok != '' and tok != ' ':
            key.append(tok)

    return key

def sort_intuitive(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)


def main():
    files = os.listdir('./PDFs')
    sort_intuitive(files)

    files = files[:-1]

    # print files[50]
    # print alphanum_key(files[50])

    pagenumbers = open('pagenumbers.txt','w')
    curr = 0

    merger = PdfFileMerger()

    for f in files:
        inp = PdfFileReader(file('./PDFs/'+f,'rb'))
        numpages = inp.getNumPages()
        pagenumbers.write(str(curr)+", "+f+"\n")
        curr += numpages

        merger.append(inp)

    merger.write('merged.pdf')

if __name__ == '__main__':
    main()
