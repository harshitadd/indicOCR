# #For installation libraries - https://medium.com/quantrium-tech/installing-tesseract-4-on-ubuntu-18-04-b6fcd0cbd78f

# from PIL import Image 
# import pytesseract 
# import sys 
# from pdf2image import convert_from_path 
# import os
# #from langdetect import detect_langs - 	print(detect_langs(text))

# # Language IDs ( tesseract )
# # Bengali (ben)
# # Gujarati (guj)
# # Hindi (hin)
# # Kannada (kan)
# # Malayalam (mal)
# # Meetei Meyak (mni)
# # Oriya (ori)
# # Punjabi (pan)
# # Santali (sat)
# # Tamil (tam)
# # Telugu (tel)



# def make_monolang(lid, s_path, d_path):
# 	PDF_file = s_path
# 	pages = convert_from_path(PDF_file, 200)  
# 	image_counter = 1
# 	for page in pages: 
# 		filename = "page_"+str(image_counter)+".jpg"
# 		page.save(filename, 'JPEG') 
# 		image_counter = image_counter + 1
# 	filelimit = image_counter-1
# 	print('Images saved')
# 	outfile = d_path + 'out' + lid + '.txt'	
# 	f = open(outfile, "a")
# 	for i in range(1, filelimit + 1): 
# 		filename = "page_"+str(i)+".jpg" 
# 		text = str(((pytesseract.image_to_string(Image.open(filename),lang=lid+'+eng'))))
# 		f.write(text) 
# 		print(i) 
# 	f.close() 


# if __name__=='__main__':
# 	lid = 'ben' #replace the language identifier ( name, string ) as required by inltk
# 	s_path = "/home/harshita/Desktop/COI-BENGALI.pdf" #replace with file path
# 	d_path = "/home/harshita/Desktop/AI4Bharat/final_output/"
# 	make_monolang(lid, s_path, d_path)


#For installation libraries - https://medium.com/quantrium-tech/installing-tesseract-4-on-ubuntu-18-04-b6fcd0cbd78f

from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os


# Language IDs ( tesseract )
# Bengali (ben)
# Gujarati (guj)
# Hindi (hin)
# Kannada (kan)
# Malayalam (mal)
# Meetei Meyak (mni)
# Oriya (ori)
# Punjabi (pan)
# Santali (sat)
# Tamil (tam)
# Telugu (tel)

def make_monolang(lid, s_path, d_path):
	PDF_file = s_path
	pages = convert_from_path(PDF_file, 300) 
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
			text = str(((pytesseract.image_to_string(Image.open(filename),lang=lid +'+eng'))))  
		except:
			skipped+=1
			text =''
		f.write(text) 
	f.close() 



if __name__=='__main__':
	lid_t = 'mal' #replace the language identifier ( name, string ) as required by inltk
	s_path = "/home/harshita/Desktop/COI-MALAYALAM-201-248.pdf" #replace with file path
	d_path = "/home/harshita/Desktop/"
	make_monolang(lid_t, s_path, d_path)
