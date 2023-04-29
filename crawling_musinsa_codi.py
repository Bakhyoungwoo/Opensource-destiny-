from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import requests
import time

#갖고오고 싶은 무신사 코디 url
url = '갖고오고 싶은 무신사 코디 url'

res = requests.get(url) #홈페이지를 읽어옴
soup = BeautifulSoup(res.text, 'html.parser')  # 갖고온 홈페이지를 분석할 수 있게 함

title_list = [] #타이틀을 저장하는 배열
items = soup.find('ul', class_='style-list').find_all('li', class_='style-list-item')
for item in items:
    title = item.find('strong', class_='style-list-information__title').get_text(strip=True) #타이틀 찾아주기
    image_url = item.find('img', class_='style-list-thumbnail__img')['data-original'] #이미지url갖고옴
   

    urllib.request.urlretrieve(image_url, '{}.png'.format(title)) #url이용해서 이미지를 다운받음(이미지 저장이름은 title)