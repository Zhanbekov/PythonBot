import urllib
import pprint
import re
import requests
  
import bs4
  
r = requests.get('https://grouple.co//', auth=('Dragon Scale', '01k7fc31dkw'))
print(r.status_code)
print(r)
  
url = 'https://grouple.co//'
html = urllib.request.urlopen(url).read().decode('utf-8')
soup = bs4.BeautifulSoup(html,features="html5lib" )
  
signLink = soup.find('a', {'id': 'sign_in'})
if signLink:
    print(signLink.prettify())