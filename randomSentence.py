from bs4 import BeautifulSoup
from random import randrange
#This file generates a random sentence to be used for typing practice

import urllib.request

linkList = []
returnText = ""


fp = urllib.request.urlopen("http://www.magickeys.com/books/")
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()
soup = BeautifulSoup(mystr, features="html5lib")#make soup that is parse-able by bs
for link in soup.find_all('a'):
    candidatePage = link.get('href')
    mustContain = "http://www.magickeys.com/books/"
    if (candidatePage):
        if mustContain in candidatePage:
            if (candidatePage not in linkList):
                linkList.append(candidatePage)

randNum = randrange(len(linkList))

fp = urllib.request.urlopen(linkList[randNum])
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()
soup = BeautifulSoup(mystr, "html.parser")#make soup that is parse-able by bs
page = soup.find_all("p")
for tag in page:
    text = tag.text.split(".")
    for i in text:
        newText = i.strip() + ". "
        if len(newText) > 2:
            returnText = returnText + newText
returnText = returnText.strip()
print(returnText)
print(len(returnText))