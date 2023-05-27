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

title_list=[]
price_list=[]
items = soup.find('ul', id='searchList').find_all('li', class_='li_box') 
for i, item in enumerate(items):
    title = item.find('div', class_='article_info').find('p', class_='list_info').find('a').get_text(strip=True)#하의 타이틀
    price_tag = item.find('div', class_='article_info').find('p', class_='price')#하의 가격
    price = price_tag.get_text(strip=True) 
    if price_tag.find('del'):#del tag안의 할인 전의 가격을 찾아 공백 처리
        del_price = price_tag.find('del').get_text(strip=True) # 문자열 갖고와서 저장
        price = price.replace(del_price, '') #del_price를 공백으로 바꿔서 없앤다.
    image_url = 'https:' + item.find('img', class_='lazyload')['data-original']
    title_list.append(title)
    price_list.append(price)

    if '/' in title:
        title = title.replace('/', '-')

    urllib.request.urlretrieve(image_url, 'cloth/{}.png'.format(title)) #img파일 안에 이미지 다운

    print(title)
    print(price)
    print(image_url)

data = {'title' : title_list, 'price' : price_list} #엑셀파일에 하의 타이틀 및 가격 저장
df = pd.DataFrame(data)
df.to_excel("pants.xlsx")
