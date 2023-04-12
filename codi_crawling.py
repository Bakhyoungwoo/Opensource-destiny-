from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

url = 'https://www.lookpin.co.kr/coordi?searchKeywords%5B0%5D=%EA%B2%B0%ED%98%BC%EC%8B%9D&order=trending&page=1'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

items = soup.find('section', class_='Coordi_coordi__3fqAN').find_all('div', class_='CoordiCard_card__1pMHY')
for i, item in enumerate(items):
    title = item.find('div', class_='CoordiCard_title__xUWCe').get_text(strip=True)
    image_url = item.find('picture', class_='CoordiCard_picture__1N8ub').find('img')['src']
    
    urllib.request.urlretrieve(image_url, '{}.png'.format(i+1))
