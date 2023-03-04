import os, sys
import requests
from urllib.parse import urljoin
from urllib.parse import unquote
import re


from bs4 import BeautifulSoup
session = requests.Session()
#... whatever requests config you need here

def soupfindAllnSave( url, soup, tag2find='img', inner='src'):
    for res in soup.findAll(tag2find):   # images, css, etc..
        try:
            filename = os.path.basename(res[inner])  
            fileurl = urljoin(url, res.get(inner))
            # rename to saved file path
            # res[inner] # may or may not exist 
            print("fileurl",fileurl.replace('https://ccweb.imgix.net/',''))
            res[inner] = unquote(fileurl.replace('https://ccweb.imgix.net/',''))
        except Exception as exc:      
            print(exc, file=sys.stderr)
    return soup

def savePage(response, pagefilename='page'):    
   url = response.url
   soup = BeautifulSoup(response.text)
   soup = soupfindAllnSave( url, soup, 'img', inner='src')
   findtoure = soup.find(text = re.compile('r.p="/webpack/"'))
   fixed = findtoure.replace('r.p="/webpack/"','r.p="https://www.classcentral.com/webpack/"')
   findtoure.replace_with(fixed)
   for link in soup.find_all('a'):
        print(link.get('href'))
        if(link.get('href').startswith('/')):
            link['href'] = "https://www.classcentral.com" + link.get('href')
   with open(pagefilename+'.html', 'w') as file:
      file.write(soup.prettify())
   return soup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response = session.get('https://www.classcentral.com/',headers=headers)
savePage(response, 'index')




# message to be translated
message = "Find your next course"

# creating a EngtoHindi() object
res = EngtoHindi(message)

# displaying the translation
print(res.convert)
