import os 
import tarfile
input_path = '/home/harshitadd/gu_darts/'
years = os.listdir(input_path)
for year in years:
  year_dir = tarfile.open(year)
  year_dir.extractall(input_path)
  year_dir.close()

  
  
