from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import requests
import time

#갖고오고 싶은 무신사 코디 url
url = 'https://www.musinsa.com/search/musinsa/coordi?q=%EB%B4%84%EC%BD%94%EB%94%94&list_kind=small&sortCode=term_date&sub_sort=&page=1&display_cnt=0&saleGoods=&includeSoldOut=&setupGoods=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=&d_cat_cd=&attribute=&plusDeliveryYn='

res = requests.get(url) #홈페이지를 읽어옴
soup = BeautifulSoup(res.text, 'html.parser')  # 갖고온 홈페이지를 분석할 수 있게 함

title_list = [] #타이틀을 저장하는 배열
items = soup.find('ul', class_='style-list').find_all('li', class_='style-list-item')
for item in items:
    title = item.find('strong', class_='style-list-information__title').get_text(strip=True) #타이틀 찾아주기
    
    title_list.append(title)#title 배열의 끝에 타이틀 추가
   
print(title)   