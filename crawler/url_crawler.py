import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# lang_ids = {'Assamese', 'Bengali', 'Gujarati', 'Kannada', 'Malayalam', 'Marathi', 'Odia', 'Punjabi', 'Tamil', 'Telugu'}
# lang = 'Punjabi'
page_limit = 37
page_count = 0

urls = []
filename = '/home/harshita/AI4BharatTranslation/en_te_links.txt'
while(page_count<=page_limit):
     # url = "http://legislative.gov.in/" + lang + '?page=' + str(page_count)
     url = "https://www.tn.gov.in/documents/atoz/All?page=" + str(page_count) 
     response = requests.get(url)
     soup= BeautifulSoup(response.text, "html.parser")
     links = soup.find_all('a')  
     # print(links) 
     print("Total Links Found:",links.__len__())
     print("Page Number:" + str(page_count))
     for link in links: 
          if '.pdf' in str(link.get('onclick')):
               urls.append(str(link.get('onclick')))      
     page_count+=1

print(len(urls))
with open(filename, 'w') as f:
     f.write('\n'.join(urls))
































'''
# import scrapy
# headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
# class BrickSetSpider(scrapy.Spider):
#     name = "brickset_spider"
#     start_urls = ['http://brickset.com/sets/year-2016']

#     def start_requests(self):
#         headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
#         for url in self.start_urls:
#             yield Request(url, headers=headers)



# # import requests
# from bs4 import BeautifulSoup

# def web(page,WebUrl):
#      if(page>0):
#           print('I am In')
#           url = WebUrl
#           code = requests.get(url)
#           plain = code.text
#           s = BeautifulSoup(plain,"html.parser")
#           print(s)
#           for link in s.findAll("a", {"class’:’s-access-detail-page"}):
#                tet = link.get("title")
#                print(tet)
#                tet_2 = link.get("href")
#                print(tet_2)

# web(1,"https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles")

# import scrapy

# class spider1(scrapy.Spider):
#       name = "Wikipedia"
#       start_urls = ["https://en.wikipedia.org/wiki/Battery_(electricity)"]
#       def parse(self, response):
#             pass
'''