# Codes - https://www.loc.gov/standards/iso639-2/php/code_list.php
from sentence_splitter import SentenceSplitter, split_text_into_sentences
from indicnlp.tokenize import sentence_tokenize 
sentence_count=0
base = open('/home/harshita/Desktop/COI_Out/outeng.txt','r')
content = base.read()
content = content.replace('\n',' ')
splitter = SentenceSplitter(language='en')
sentences = splitter.split(content)
# sentences = sentence_tokenize.sentence_split(content, lang='pa') #for indic lang'
sentence_count=len(sentences)
print(sentence_count)
f = open('/home/harshita/Desktop/COI_Out/outeng_split.txt','a')
for s in sentences:
	f.write(s)
	f.write('\n')


