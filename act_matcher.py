import re
lang_ids = {'Assamese', 'Bengali', 'Gujarati', 'Kannada', 'Malayalam', 'Marathi', 'Odia', 'Punjabi', 'Tamil', 'Telugu'}
for lang in lang_ids:  
	filename = '/home/harshita/AI4BharatTranslation/links/' + lang + '_links.txt'
	try: 
		with open(filename, 'r') as f:

		    links = f.read()
		    links = links.split()		    
		  	# print(str(len(links)) + ' Acts For ' + lang )
		    
		    for link in links:
		    	link = link.replace('%20',' ') 
		     	link = link.replace('%28',' ')
		     	link = link.replace('%29',' ')
		     	link = link.replace('%2C',' ')

	except: 
		print('Could not open for ' + lang)

