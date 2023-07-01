from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph

def main():
	reportName = input("Please Enter a Preferred Report Name:\n")
	inputText = input("Please Enter the Input File:\n")
	try:
		generateReport(reportName)
		print("Successfully created report")
	except:
		print("Error in creating report")

def generateReport(rN,iT):
	c = Canvas(f'{rN}.pdf',pagesez==LETTER)
	c.setTitle(rN)
	y = 700
	t = open(f'{iT}','r')
	for line in t:
		c.drawString(100,y,line.strip())
	c.save()
