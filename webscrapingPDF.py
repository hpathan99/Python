
from PyPDF2 import PdfReader

pdf_reader = PdfReader("project_nbody.pdf")
page = pdf_reader.pages[0]

text = page.extract_text()
print(text)