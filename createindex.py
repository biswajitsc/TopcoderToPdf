import os

texcode = ""
texcode += "\
\\documentclass[twocolumn]{article}\n\
\\usepackage[pageanchor]{hyperref}\n\
\\usepackage{lipsum}\n\
\\usepackage{pdfpages}\n\
\\setlength{\\evensidemargin}{-0.5in}\n\
\\setlength{\\headheight}{0in}\n\
\\setlength{\\headsep}{0in}\n\
\\setlength{\\oddsidemargin}{-0.5in}\n\
\\setlength{\\paperheight}{11in}\n\
\\setlength{\\paperwidth}{8.5in}\n\
\\setlength{\\tabcolsep}{0in}\n\
\\setlength{\\textheight}{9.5in}\n\
\\setlength{\\textwidth}{7.5in}\n\
\\setlength{\\topmargin}{-0.3in}\n\
\\setlength{\\topskip}{0in}\n\
\\setlength{\\voffset}{0.1in}\n\
\\begin{document}\n\
\n\
\\title{TopCoder Problems Database}\n\
\\author{by InvisibleGuy\\thanks{works at Nowhere}}\n\
\\date{6th August 2015}\n\
\\maketitle\n\
\\pagebreak\n\
\n\
{\n\
    \\Huge Index\n\
    \\vspace{1cm}\n\
}\n\
\n\
"

srmtexcode = texcode.replace('Database','Database: SRMs')
othertexcode = texcode.replace('Database', 'Database: Excluding SRMs')

srmpages = open('./Merged/srmpagenumbers.txt','r')
srmoffset = 23

for line in srmpages.readlines():
    line = line.split(',, ')
    line[0] = str(int(line[0])+srmoffset)
    line[1] = line[1].replace('&','\&')
    line[1] = line[1].replace('.pdf','')
    line[1] = line[1].replace('Round 1 ','')

    srmtexcode += "\\hyperlink{page."+line[0]+"}{"+line[1]+"}\n\n"

srmtexcode += "\
\\pagebreak[2]\n\
\\includepdf[pages=-]{srmmerged.pdf}\n\
\\end{document}\
"

srmtexfile = open('./Merged/TopcoderSRMs.tex','w')
srmtexfile.write(srmtexcode)
srmtexfile.close()


otherpages = open('./Merged/otherpagenumbers.txt','r')
otheroffset = 17

for line in otherpages.readlines():
    line = line.split(',, ')
    line[0] = str(int(line[0])+otheroffset)
    line[1] = line[1].replace('&','\&')
    line[1] = line[1].replace('.pdf','')

    othertexcode += "\\hyperlink{page."+line[0]+"}{"+line[1]+"}\n\n"

othertexcode += "\
\\pagebreak[2]\n\
\\includepdf[pages=-]{othermerged.pdf}\n\
\\end{document}\
"

othertexfile = open('./Merged/TopcoderOthers.tex','w')
othertexfile.write(othertexcode)
othertexfile.close()
