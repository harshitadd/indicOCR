# Codes - https://www.loc.gov/standards/iso639-2/php/code_list.php - Equipped to handle eng codeswitching only 
import re 
from sentence_splitter import SentenceSplitter, split_text_into_sentences
from indicnlp.tokenize import sentence_tokenize 
sentence_count=0
lid = 'hin' #CHANGE THIS 
file = '/home/harshita/Desktop/COI_Out/out' +lid+'.txt'
base = open(file,'r')
content = base.read()
patterns= ['( . .)+','-+','%','[A-Z]+','[a-z]+',' \* ','\d{1}\.\d{1}','#','\d{1}','(\d{2}#)', '(\d{3}#)', '(\d{2}.)', '(\d{3}.)', '\d{2}', '\d{3}', '\.\.+', '\[','\]','\[\]' ] #CHANGE THIS IF THE LANGUAGE USES . as delimeter
for pattern in patterns:
	content = re.sub(pattern,'',content)
content = re.sub('  +','',content)
content = content.replace('\n','')
sentences = sentence_tokenize.sentence_split(content, lang='hi') # CHANGE THIS
final = ''
for s in sentences:
	final+=s
	final+='\n'
sentence_count=len(sentences)
print(sentence_count)
n = '/home/harshita/Desktop/out' + lid + '_split.txt'
f = open(n,'w')
f.write(final)
	