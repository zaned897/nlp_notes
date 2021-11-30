#%%
import PyPDF2
from wasabi import Printer
msg = Printer()

def write_text(text, file_path):
	"""Write the text of the pdf file."""
	with open(file_path, 'wb') as file:
		file.write(text)
	return True

def read_file(file_path):
	"""Read and keep open the pdf file."""
	file = open(file_path, 'rb')
	pdf_reader = PyPDF2.PdfFileReader(file)
	return pdf_reader, file

def close_file(file):
	"""Close the pdf file."""
	try:
		file.close()
	except FileNotFoundError:
		msg.fail('File not found')
		return False
	return True

def get_text(pdf_reader, page):
	"""Return the text of the pdf file."""
	try: 
		text = pdf_reader.getPage(page).extractText()
	except IndexError:
		msg.fail('Page not found')
		return False
	return pdf_reader.getPage(page).extractText()

def get_all_text(pdf_reader):
	"""Return the text of all pages of the pdf file in a list."""
	text = []
	for page in range(pdf_reader.numPages):
		text.append(pdf_reader.getPage(page).extractText())
	return text

if __name__ == '__main__':
	file = '../resources/PDFFiles/US_Declaration.pdf'
	page = 0
	pdf_reader, file = read_file(file)
	single_page_text = get_text(pdf_reader, page=page)
	all_pages_text = get_all_text(pdf_reader)
	print(single_page_text)
