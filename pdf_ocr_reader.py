# For installation libraries - https://medium.com/quantrium-tech/installing-tesseract-4-on-ubuntu-18-04-b6fcd0cbd78f
# Source - http://legislative.gov.in/constitution-of-india-in-regional-languages
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os


# Language IDs ( tesseract )
# Bengali (ben) *** Done
# Gujarati (guj) ** Done
# Hindi (hin) ** Done 
# Kannada (kan)
# Marathi (mar) ** Done 
# Malayalam (mal)** Done 
# Oriya (ori)
# Punjabi (pan) ** Done 
# Tamil (tam)
# Telugu (tel) 
# Assamese (asm)
# English (eng) ** Done 
# Urdu (urd) ** Dropped 

def make_monolang(lid, s_path, d_path):
	PDF_file = s_path
	pages = convert_from_path(PDF_file, 250) 
	image_counter = 1
	skipped = 0
	for page in pages: 
		filename = "page_"+str(image_counter)+".jpg"
		page.save(filename, 'JPEG') 
		image_counter = image_counter + 1
	filelimit = image_counter-1
	print('Images converted')
	outfile = d_path + 'out' + lid + '.txt'
	f = open(outfile, "a") 
	for i in range(1, filelimit + 1):
		print(i) 
		filename = "page_"+str(i)+".jpg" 
		try:
			text = str(((pytesseract.image_to_string(Image.open(filename),lang=lid+'+eng'))))  # to 
		except:
			skipped+=1
			text =''
		f.write(text) 
	f.close() 



if __name__=='__main__':
	lid_t = 'asm' #replace the language identifier ( name, string ) as required by inltk
	s_path = "/home/harshita/Desktop/COI-ASSAMESE-251-284.pdf" #replace with file path
	d_path = "/home/harshita/Desktop/"
	make_monolang(lid_t, s_path, d_path)
