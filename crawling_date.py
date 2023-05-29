from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import pandas as pd

#갖고오고 싶은 무신사 코디 url
url = 'https://www.musinsa.com/search/musinsa/coordi?q=%EB%8D%B0%EC%9D%B4%ED%8A%B8%EB%A3%A9&list_kind=small&sortCode=term_date&sub_sort=&page=1&display_cnt=0&saleGoods=&includeSoldOut=&setupGoods=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=&d_cat_cd=&attribute=&plusDeliveryYn='

headers = {
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

res = requests.get(url) #홈페이지를 읽어옴
soup = BeautifulSoup(res.text, 'html.parser')  # 갖고온 홈페이지를 분석할 수 있게 함

title_list = [] #타이틀을 저장하는 배열
items = soup.find('ul', class_='style-list').find_all('li', class_='style-list-item')
for item in items:
    title = item.find('strong', class_='style-list-information__title').get_text(strip=True) #타이틀 찾아주기
    image_url = item.find('img', class_='style-list-thumbnail__img')['data-original'] #이미지url갖고옴
    title_list.append(title)#title 배열의 끝에 타이틀 추가

    urllib.request.urlretrieve(image_url, 'codi/{}.png'.format(title)) #url이용해서 이미지를 다운받음(이미지 저장이름은 title)
print(image_url)

data = {'title' : title_list}
df = pd.DataFrame(data)
df.to_excel("winter.xlsx") 
