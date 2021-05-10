# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('examen parcial-administracion financiera.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
a = pageObj.extractText().replace("\n", "").split(" ")
print(a) 
  
# closing the pdf file object 
#pdfFileObj.close() 
