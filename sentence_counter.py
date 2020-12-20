# Importing required modules
# import codecs
# with codecs.open(r'C:\Users\ihsra\Downloads\COI-HINDI.pdf', encoding='utf-8') as f:
#     txt = f.read()

# print(txt)

import PyPDF2
import sys
sc=0
# Creating a pdf file object
pdfFileObj = open(r'C:\Users\ihsra\Downloads\COI-HINDI.pdf','rb')
# Creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# Getting number of pages in pdf file
pages = pdfReader.numPages
# Loop for reading all the Pages
for i in range(pages):
        # Creating a page object
        pageObj = pdfReader.getPage(i)
        # Printing Page Number
        # print("Page No: ",i)
        # Extracting text from page
        # And splitting it into chunks of lines
        text = pageObj.extractText().split('\n')
        # final = text.decode
        # sys.stdout.buffer.write(text.encode('UTF-8'))
        # Finally the lines are stored into list
        # For iterating over list a loop is used
        for i in range(len(text)):
                # Printing the line
                # Lines are seprated using "\n"
                sc+=1
                text[i]
                # print(text[i],end="\n")
                
        # For Seprating the Pages
        # print()
print('Total Number of Sentences: ' + str(sc))
# s = text[i].encode('utf-8')
# print(s)


# import fitz
# doc = fitz.open(r'C:\Users\ihsra\Downloads\COI-HINDI.pdf')
# txt = doc.getPageText(0)
# txt






























# # import PyPDF4
# # import re
# # import io

# # pdfFileObj = open(r'C:\Users\ihsra\Downloads\COI-updated.pdf', 'rb')

# # pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

# # pageObj = pdfReader.getPage(0)
# # pages_text = pageObj.extractText()
# # print(pages_text)
# # sentence_count = 0 
# # for line in io.StringIO(pages_text):
# #     print(line)

# import PyPDF2
# pdfFileObj = open('C:\Users\ihsra\Downloads\COI-updated.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pages = pdfReader.numPages
# pages
# text = pageObj.extractText()
# sentence_count=0
# for i in range(pages):
#         # Creating a page object
#         pageObj = pdfReader.getPage(i)
#         # Printing Page Number
#         print("Page No: ",i)
#         # Extracting text from page
#         # And splitting it into chunks of lines
#         text = pageObj.extractText().split("\n \n ")
#         # Finally the lines are stored into list
#         # For iterating over list a loop is used
#         for i in range(len(text)):
#                 # Printing the line
#                 # Lines are seprated using "\n"
#                 print(text[i],end=" ")
        
# from PyPDF2 import PdfFileReader

# pdf_document = r"C:\Users\ihsra\Downloads\COI-updated.pdf"

# with open(pdf_document, "rb") as filehandle:
#     pdf = PdfFileReader(filehandle)
#     info = pdf.getDocumentInfo()
#     pages = pdf.getNumPages()

#     print (info)
#     print ("number of pages: %i" % pages)
#     print('#################################################################')
    
#     for page in pages: 

# page1 = pdf.getPage(4)
#     print(page1)
#     print(page1.extractText())


# from PyPDF2 import PdfFileReader, PdfFileWriter

# pdf_document = r"C:\Users\ihsra\Downloads\COI-updated (1).pdf"

# pdf = PdfFileReader(pdf_document)

# for page in range(pdf.getNumPages()):
#     pdf_writer = PdfFileWriter
#     current_page = pdf.getPage(page)
#     pdf_writer.addPage(current_page)

#     outputFilename = "example-page-{}.pdf".format(page + 1)
#     with open(outputFilename, "wb") as out:
#         pdf_writer.write(out)

#         print("created", outputFilename)
