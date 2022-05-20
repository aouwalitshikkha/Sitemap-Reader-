from bs4 import BeautifulSoup as bs
from requests import get

url = input("Enter URL: ")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'referer': 'https://www.sitename.com'
    }

response = get(url , headers = headers).text
html = bs(response, 'html.parser')
allloc= html.findAll('loc')
allsitemap = []

for loc in allloc:
    allsitemap.append(loc.text)
    with open('copy.txt', 'a+') as file:
        file.writelines(loc.text+'\n')
        file.close()
