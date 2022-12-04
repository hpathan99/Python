import requests
import PyPDF2

#download pdf file using requests library
#url of pdf goes here
pdf_url = ''
response = requests.get(pdf_url)

#save pdf data to file
with open('nameofpdffile','wb') as f:
    f.write(response.content)

pdf_file = open('nameofpdffile', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

for page in pdf_reader.pages:
    page_text = page.extractText()
    print(page_text)