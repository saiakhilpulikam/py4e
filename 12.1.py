import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_88770.html').read()
soup = BeautifulSoup(html, "html.parser")
spans = soup('span')
numbers = []
for span in spans:
    numbers.append(int(span.string))
print(sum(numbers))
