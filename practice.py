<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import operator

def start_the_crawl(url):
    word_list=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code)

    for plain_text in soup.find_all('a'):
        content=plain_text.string
        words=str(content).lower().split()

        for word in words:
            word_list.append(word)
            print(word)

=======
import requests
from bs4 import BeautifulSoup
import operator

def start_the_crawl(url):
    word_list=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code)

    for plain_text in soup.find_all('a'):
        content=plain_text.string
        words=str(content).lower().split()

        for word in words:
            word_list.append(word)
            print(word)

>>>>>>> c3a581a6142b4afe5141cc94fd60406c12aa70fe
start_the_crawl('http://www.10minuteschool.com')