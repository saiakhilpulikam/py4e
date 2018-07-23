import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

taglist=list()
url=input("Enter URL: ")
count=int(input("Enter count:"))
position=int(input("Enter position:"))
for i in range(count):
    print ("Retrieving:",url)
    html = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    for tag in tags:
        taglist.append(tag)
    url = taglist[position-1].get('href', None)
    del taglist[:]
print ("Retrieving:",url)
