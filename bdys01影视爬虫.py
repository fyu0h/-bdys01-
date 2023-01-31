import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

driver = webdriver.Chrome('/usr/local/chromedriver')
domain = 'https://www.bdys01.com/guoju/23065.htm'
driver.get(domain)
time.sleep(5)
DOM = driver.page_source

soup = BeautifulSoup(DOM, 'html.parser')
torrent_list = soup.find_all(id='torrent-list')
prefix = "https://www.bdys01.com"

links = [prefix + link for torrent in torrent_list for link in re.findall(r'(?<=href=").*?(?=")', str(torrent))]
for link in links:
    print(link)
