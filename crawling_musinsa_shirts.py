from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

url = 'https://www.musinsa.com/categories/item/001' #해당 URL갖고옴
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

title_list=[] #타이틀을 저장할 배열 생성
price_list=[] #가격을 저장할 배열 생성
items = soup.find('ul', id='searchList').find_all('li', class_='li_box') 
for i, item in enumerate(items):
    title = item.find('div', class_='article_info').find('p', class_='list_info').find('a').get_text(strip=True)#상의 타이틀
    price_tag = item.find('div', class_='article_info').find('p', class_='price')#하의 가격
    price = price_tag.get_text(strip=True) #가격 추출
    title_list.append(title)
    price_list.append(price)
    
    
print(title) #콘솔창에 타이틀 출력
print(price) #콘솔창에 가격 출력

