<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
'''
def trade_spider(max_pages, base_url):
    page=1
    while page<max_pages:
        url=base_url+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.find_all('a',{'class':'item-name'})
            href=link.get('href')
        page+=1
        '''


def url_spider(url,number_of_links):
    urln=1
    while urln<number_of_links:
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")
        for link in soup.find('a'):
            href=link.get('href')
            print(href)
            urln+=1

url_spider('http://www.next.co.uk',1000)






=======
import requests
from bs4 import BeautifulSoup
'''
def trade_spider(max_pages, base_url):
    page=1
    while page<max_pages:
        url=base_url+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.find_all('a',{'class':'item-name'})
            href=link.get('href')
        page+=1
        '''


def url_spider(url,number_of_links):
    urln=1
    while urln<number_of_links:
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")
        for link in soup.find('a'):
            href=link.get('href')
            print(href)
            urln+=1

url_spider('http://www.next.co.uk',1000)






>>>>>>> c3a581a6142b4afe5141cc94fd60406c12aa70fe
