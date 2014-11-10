from bs4 import BeautifulSoup
from pyquery import PyQuery
import requests
import sys

from settings import mysql_connection

url = sys.argv[1]

response = requests.get(url)
# pq = PyQuery(response.content)
# pattern for http://www.drupalshowcase.com/

bs = BeautifulSoup(response.content)
links = bs.find_all('a')
for link in links:
    href = link
    print href
    #if href:
    #    if href.startswith('http'):
    #        print href
