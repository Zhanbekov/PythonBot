import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)  #Response
    return r.text #returns only html code of the page (url)

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    tds = soup.find('table').find.all('td', class_='navbar navbar-default')
    
    links = []

    for td i





def main():
    # https://coinmarketcap.com/all/views/all/
  all_links = []





if __name__ == '__main__':
    main()