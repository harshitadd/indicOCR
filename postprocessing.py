# Only for English
import re 
from sentence_splitter import SentenceSplitter, split_text_into_sentences
file = '/home/harshita/Desktop/COI_Out/outeng.txt'
base = open(file,'r')
content = base.read()
patterns= ['-+','%',' \* ','\d{1}\.\d{1}','#','\d{1}','(\d{2}#)', '(\d{3}#)', '(\d{2}\.)', '(\d{3}\.)', '\d{2}', '\d{3}']
for pattern in patterns:
	content = re.sub(pattern,'',content)
content = content.replace('\n',' ')
splitter = SentenceSplitter(language='en')
sentences = splitter.split(content)
final = ''
for s in sentences:
	final+=s
	final+='\n'
sentence_count=len(sentences)
print(sentence_count)
f = open('/home/harshita/Desktop/COI_Final/outeng_split.txt','w')
f.write(final)
