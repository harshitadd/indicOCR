from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
PDF_file = r"C:\Users\ihsra\Downloads\COI-MALAYALAM.pdf" 
pages = convert_from_path(PDF_file, 4) 
image_counter = 1
for page in pages: 
    filename = "page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG') 
    image_counter = image_counter + 1
filelimit = image_counter-1
outfile = r"C:\Users\ihsra\Downloads\out_text.txt"
f = open(outfile, "a") 
for i in range(1, filelimit + 1): 
    filename = "page_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename))))) 
    text = text.replace('-\n', '')     
    f.write(text) 
f.close() 
