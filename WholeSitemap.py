from bs4 import BeautifulSoup as bs
from requests import get

url = input("Enter URL: ")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'referer': 'https://www.wikibio.us'
    }

response = get(url , headers = headers).text
html = bs(response, 'html.parser')
firstlevel= html.findAll('loc')
firstlist = []

for level in firstlevel:
    firstlist.append(level.text)


for url in firstlist:
    response = get(url , headers = headers).text
    html = bs(response, 'html.parser')
    alllocs= html.findAll('loc')
    for surl in alllocs:
        with open('copy.txt', 'a+') as file:
            file.writelines(surl.text+'\n')
            file.close()
