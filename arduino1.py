#!/usr/bin/env python3
'''
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import *
url='https://en.wikipedia.org/wiki/List_of_investments_by_Microsoft_Corporation'
directory = '/home/suba/Documents/Arduino/WebScrapingBootCamp/'
def scrape(url, name):
    f=requests.get(url)
    bsobj = bs(f.content, 'html.parser')
    name=str(bsobj.title)[7:-8]
    websiteName = urlparse(url)[1]+'/'
    s=directory+name+'.html'
    with open(s,'wb') as obj:
        obj.write(f.content)
    links = getLinks(websiteName,bsobj)
    print(links)
    return True
def getLinks(websiteName, bsobj):
    links=list()
    for link in bsobj.find_all('a'):
        if 'href' in link.attrs:
            links.append(urljoin(websiteName, link.attrs['href']))
        return links
val = scrape(url, directory)

import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/List_of_investments_by_Microsoft_Corporation'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    print(link.get('href'))

import requests
from bs4 import BeautifulSoup
urls = 'https://en.wikipedia.org/wiki/List_of_investments_by_Microsoft_Corporation'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

# opening a file in write mode
f = open("test1.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   f.write(data)
   f.write("\n")

f.close()

import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/List_of_investments_by_Microsoft_Corporation'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
def link50(url):
    global links
    f = open('test1.txt', 'w')
    for link in soup.find_all('a'):
        data=link.get('href')
        f.write(str(data))
        f.write('\n')
    f.close()
    links=[]
    f = open('test1.txt', 'r')
    for x in f.readlines():
        if 'https://' in x:
            links.append(x)
        elif 'http://' in x:
            links.append(x)
    f.close()
    return links
total=[]
if len(links)<=50:
    for x in range(len(links)):
        total.append(link50(links[x]))
print(total,'\n'*4,links)
'''
