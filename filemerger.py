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

    srms = []
    others = []
    for f in files:
        if f.startswith('Single Round Match'):
            srms.append(f)
        else:
            others.append(f)

    # print files[50]
    # print alphanum_key(files[50])

    srmpagenumbers = open('./Merged/srmpagenumbers.txt','w')
    otherpagenumbers = open('./Merged/otherpagenumbers.txt','w')

    curr = 0
    merger = PdfFileMerger()

    for f in srms:
        inp = PdfFileReader(file('./PDFs/'+f,'rb'))
        numpages = inp.getNumPages()
        srmpagenumbers.write(str(curr)+",, "+f+"\n")
        curr += numpages

        merger.append(inp)

    merger.write('./Merged/srmmerged.pdf')


    curr = 0
    merger = PdfFileMerger()

    for f in others:
        inp = PdfFileReader(file('./PDFs/'+f,'rb'))
        numpages = inp.getNumPages()
        otherpagenumbers.write(str(curr)+",, "+f+"\n")
        curr += numpages

        merger.append(inp)

    merger.write('./Merged/othermerged.pdf')

    srmpagenumbers.close()
    otherpagenumbers.close()

if __name__ == '__main__':
    main()
