from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup 

from selenium import webdriver 
import time 


# https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

#page source를 html에 담아야함 
html = driver.page_source
soup = BeautifulSoup(html) 

insta = soup.select('')

driver.close()



