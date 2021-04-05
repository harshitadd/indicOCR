# import os 
# import tarfile
# input_path = '/home/harshitadd/gu_darts/'
# years = os.listdir(input_path)
# for year in years:
#   year_dir = tarfile.open(year)
#   year_dir.extractall(input_path)
#   year_dir.close()

import json
import os 
year = '2019' 
months = os.listdir('/home/harshitadd/en_darts/' + year)
for month in months:
  days = os.listdir('/home/harshitadd/en_darts/' + year + '/' + month + '/')
  for day in days:
    articles = os.listdir('/home/harshitadd/en_darts/' + year + '/' + month + '/' + day + '/')
    for article in articles:
      sentences = []
      input_path = '/home/harshitadd/en_darts/' + year + '/' + month + '/' + day + '/' + article 
      with open(input_path) as f:
        try: 
          data = json.load(f)
          sentences.append('\n'.join(data['sentences']))
          file_input_name = '/home/harshitadd/dated_sentences/'+ day + '_' + month + '_' + year + '_sentences.txt' 
          with open(file_input_name,'a') as file:
              file.write('\n'.join(sentences)) 
        except:
          print('Failed for ' +  year + '/' + month + '/' + day + '/' + article)

          
  
