# TopcoderToPDF Crawler
Crawls Topcoder problems and compiles into a single PDF file for portability.

Documentation
------------
* ```topcoderParse.py``` crawls the topcoder archive and saves the htmls in the folder ```htmls```.
* ```topcoderGenPdf.py``` cleans the htmls and uses ```pdfkit``` to generate pdfs for all the files into the ```PDFs``` folder.
* ```filemerger.py``` merges the pdfs into single files. This produces two files ```srmmerged.pdf``` and ```othermerged.pdf``` for SRMs and non-SRMs respectively.
* ```createindex.py``` generates the LaTeX code for the final pdfs of the two files. This also includes a generated index for easy navigation.
* The command ```pdflatex Topcoder<X>.tex``` compiles the LaTeX documents to the final PDFs. ```X``` stands for SRMs and Others. The final PDFs are named as ```TopcoderSRMs.pdf``` and ```TopcoderOthers.pdf```.
* To make this behind a proxy uncomment the proxy option in the following lines of the file ```topcoderGenPdf.py``` and set the proper proxy.

    ```
    options = {
	    'page-size': 'A5',
	    'margin-top': '0.30in',
	    'margin-right': '0.0in',
	    'margin-bottom': '0.30in',
	    'margin-left': '0.0in',
	    'cache-dir': 'html_cache',
	    # 'proxy': '10.3.100.207:8080'
	}
	```
