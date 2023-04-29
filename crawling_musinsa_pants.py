from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time

url = 'https://www.musinsa.com/categories/item/003' #해당 URL갖고옴
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')


title_list = [] #타이틀을 저장하는 배열
items = soup.find('ul', id='searchList').find_all('li', class_='li_box') 
for i, item in enumerate(items):
    title = item.find('div', class_='article_info').find('p', class_='list_info').find('a').get_text(strip=True)#타이틀 찾아오기
    image_url = 'https:' + item.find('img', class_='lazyload')['data-original']#이미지url갖고옴

    urllib.request.urlretrieve(image_url, '{}.png'.format(title)) #url이용해서 이미지를 다운받음
