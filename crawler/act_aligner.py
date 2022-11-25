import re
actno_year = []
lid = []
lang_ids = {'Assamese', 'Bengali', 'Gujarati', 'Kannada', 'Malayalam', 'Marathi', 'Odia', 'Punjabi', 'Tamil', 'Telugu'}
for lang in lang_ids:  
	filename = '/home/harshita/AI4BharatTranslation/links/' + lang + '_links.txt'
	try: 
		with open(filename, 'r') as f:

			links = f.read()	
			links = links.split()

			print(str(len(links)) + ' Acts For ' + lang )

			for link in links:
				link = link.replace('%20',' ') 
				link = link.replace('%28',' ')
				link = link.replace('%29',' ')
				link = link.replace('%2C',' ')
				link = link.replace(' of ','-')
				link = link.replace('pt 1','_0')
				link = link.replace('pt 2','_1')
				year = re.findall('(\d{4})', link)
				actno = re.findall('\d{2}',link)
				
				print(link[46:])

	except: 
		print('Could not open for ' + lang)
