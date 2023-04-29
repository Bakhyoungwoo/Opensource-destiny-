from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
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
title_list.append(title)

if'/' in title:
    title=title.relplace('/', '-')# title에 '/'가 들어간 옷 때문에 오류 발생 '-'로 대체

    urllib.request.urlretrieve(image_url, 'img/{}.png'.format(title)) #url이용해서 이미지를 다운받음

    print(title)
    print(image_url)

data = {'title': title_list} #엑셀파일에 하의 타이틀 저장
df=pd.DataFrame(data)
df.to_excel("pants.xlsx")
