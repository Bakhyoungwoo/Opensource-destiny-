from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time
import re

url = 'https://www.musinsa.com/app/goods/2628632'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

