# NEED TO INSTALL PYPDF


import pyPDF

def getPDFContent(path):
	content = ""
	#load the pdf in pyPDF
	pdf = pyPDF.PDFFileReader(file(path,"rb"))
	# iterate through the pages
	for i in range(0, pdf.getNumPages()):
		content += pdf.getPage(i).extractText() + "\n"

	content = " ".join(content.replace(u"\xa0")," ").strip().split()
	return content

print getPDFContent("test.pdf").encode("ascii","ignore")