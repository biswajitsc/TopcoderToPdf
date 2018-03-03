# TopcoderToPDF Crawler
Crawls/downloads algorithmic problems from the Topcoder problem archive and compiles them into a single PDF file for portability.

__Note:__ This project is no longer active. If you are using this and it does not work, please try to fix it yourself.

Library requirements
------------
* pdfkit
* PyPDF2

__Note:__ After cloning the repository, you need to run ```git submodule update --init --recursive``` to fetch the PyPDF2 submodule. Install the version of PyPDF2 that is provided in this repository. The newer versions do not seem to work in this situation.

Documentation and working steps
------------
* ```topcoderParse.py``` crawls the topcoder archive and saves the htmls in the folder ```htmls```.
* Downloading all the problems can take a lot of time and can even fail. In that case one might stop and rerun the program. Before re-running the program, set ```done = x``` in ```topcoderParse.py```, where ```x``` denotes the number of problems to skip downloading. Note that the program prints the problem number of the problem being downloaded, so set ```done``` as the problem number of the last successful download. This way it will skip downloading the problems already downloaded.
* ```topcoderGenPdf.py``` cleans the htmls and uses ```pdfkit``` to generate pdfs for all the files into the ```PDFs``` folder.
* ```filemerger.py``` merges the pdfs into single files. This produces two files ```srmmerged.pdf``` and ```othermerged.pdf``` for SRMs and non-SRMs respectively.
* ```createindex.py``` generates the LaTeX code for the final pdfs of the two files. This also includes a generated index for easy navigation.
* The command ```pdflatex Topcoder<X>.tex``` compiles the LaTeX documents to the final PDFs. ```X``` stands for SRMs and Others. The final PDFs are named as ```TopcoderSRMs.pdf``` and ```TopcoderOthers.pdf```.
* To make this work behind a proxy, uncomment the proxy option in the following lines of the file ```topcoderGenPdf.py``` and set the proper proxy address.

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
