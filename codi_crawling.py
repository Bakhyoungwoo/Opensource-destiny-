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
