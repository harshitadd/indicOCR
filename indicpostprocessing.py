# Codes - https://www.loc.gov/standards/iso639-2/php/code_list.php - Equipped to handle eng codeswitching only 
# http://www.unicode.org/charts/ - For delimeters 
# Removing 1st x pages == with indices
# from inltk.inltk import setup 
# from inltk.inltk import tokenize
# setup('hi')

import re 
from sentence_splitter import SentenceSplitter, split_text_into_sentences
from indicnlp.tokenize import sentence_tokenize 
# # List of official delimeters
# delim = {'hin':'।'}
sentence_count=0
poorna = ['hin','ben']
lid = 'ben' #CHANGE THIS 
file = '/home/harshita/Desktop/COI_Out/out' +lid+'.txt'
base = open(file,'r')
content = base.read()
if lid in poorna:
	patterns = ['/','\.','!  ','=','>>','“;','—',',','&',' \| ','\(\)','\)','\(  \)','\(','-+','%','[A-Z]+','[a-z]+',' \* ','#','\d{1}','(\d{2}\.)','(\d{4}\.)','(\d{3}\.)','(\d{1}\.)','(\d{2}#)', '(\d{3}#)','\d{4}','\d{3}','\d{2}','\d{4,}','\[','\]','\[\]' ] 
else: 
	patterns = ['/','!  ','=','>>','“;','—',',','&',' \| ','\(\)','\)','\(  \)','\(','-+','%','[A-Z]+','[a-z]+',' \* ','#','\d{1}','(\d{2}\.)','(\d{4}\.)','(\d{3}\.)','(\d{1}\.)','(\d{2}#)', '(\d{3}#)','\d{4}','\d{3}','\d{2}','\d{4,}','\[','\]','\[\]' ] #CHANGE THIS IF THE LANGUAGE USES . as delimeter - For languages which have Poorna Virama as delimet
for pattern in patterns:
	content = re.sub(pattern,' ',content)
content = content.replace('\n', '  ')
content = content.replace('|','।')
content = re.sub('( \.)',' ',content)
content = re.sub('( . . .)+',' ',content)

sentences = sentence_tokenize.sentence_split(content, lang='bn') # CHANGE THIS
final = ''
for s in sentences:
	final+=s
	final+='\n'
final+='.EOA'
sentence_count=len(sentences)
print(sentence_count)



n = '/home/harshita/Desktop/out' + lid + '_split.txt'
f = open(n,'w')
f.write(final)
# f.write(''.join(content))
# 	