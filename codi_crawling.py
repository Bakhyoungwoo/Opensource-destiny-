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

title_list = []
codi_list = []

items = soup.find('section', class_='Coordi_coordi__3fqAN').find_all('div', class_='CoordiCard_card__1pMHY')
for i, item in enumerate(items):
    title = item.find('div', class_='CoordiCard_title__xUWCe').get_text(strip=True)
    image_url = item.find('picture', class_='CoordiCard_picture__1N8ub').find('img')['src']
    
    urllib.request.urlretrieve(image_url, '{}.png'.format(i+1))

     codi = ''
    temp = item.find('div', class_='CoordiCard_tags__2XVPv').find_all('a')
    for a in temp:
        codi += a.get_text(strip=True) + ', '
    codi = codi[:-2]
    title_list.append(title)
    codi_list.append(codi)

 # 배열에 저장된 데이터들을 pandas라이브러리를 활용하여 엑셀에 저장
data = {'title' : title_list,'codi' : codi_list} 
    
df = pd.DataFrame(data)

df.to_excel("codi_data.xlsx")
