from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time
import re

url = 'https://www.musinsa.com/app/goods/2628632'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

body_list = []
size_list = []
items = soup.find('div', class_='review-list-wrap').find_all('div', class_='review-list')
for item in items:
    body = item.find('div', class_='review-profile__text-wrap').find('div', class_="review-profile__information").find('p').get_text(strip=True)
    size = item.find('div', class_='review-goods-information').find('div', class_='review-goods-information__item').find('p').get_text(strip=True)
    body_list.append(body)
    size_list.append(size)
    
    print(body)
    print(size)
    
data = {'body': body_list, 'size': size_list}
df = pd.DataFrame(data)
df.to_excel("size.xlsx")

