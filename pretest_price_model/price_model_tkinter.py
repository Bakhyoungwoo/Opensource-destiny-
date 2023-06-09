from tkinter import *
import tkinter as tk
from tkinter import Label,Entry,Button
import pandas as pd
from difflib import get_close_matches
from PIL import Image, ImageTk
import os
import random
from openpyxl import *


root = Tk()
root.title("의류 추천 프로그램")
root.geometry("1300x1000")

global words_list

def create_price_window():
    price_page=Tk()
    price_page.title("test1")
    price_page.geometry("1300x1000")
    df = pd.read_excel('example.xlsx')
    
    # 사용자로부터 옷 이름을 입력받음
    label_cloth_name = Label(price_page,text="옷 이름을 입력하세요: ")
    label_cloth_name.place(x=100,y = 20)
    price_name = Entry(price_page,width = 20)
    price_name.place(x=100,y = 40)
    price_name.insert(0,"ex : 무신사 스탠다드")
    
    name_lower = None
    name = None
    def btnsave_price_name():
        #전역변수 설정
        global name_lower
        global name
        name = price_name.get()  # Get the cloth name from the Entry widget and convert to lowercase
        # 영어 이름의 경우 대소문자 구분 없이 옷 이름을 입력할 수 있도록 입력한 이름을 소문자로 변환
        name_lower = name.lower()
        return name_lower, name
    #현재 btnsave_price_name에서만 값이 저장되는 사태발생
    btn_price_name = Button(price_page, text="click", command=btnsave_price_name)
    btn_price_name.place(x=400,y=40)
    
    cloth_name_lower,cloth_name = btnsave_price_name()
    print(cloth_name_lower,cloth_name)
    

    # title열에서 옷 이름이 일치하는 행을 찾음
    matching_rows = df.loc[df['title'].str.lower() == cloth_name_lower]

    # 가격 정보를 담을 리스트를 생성
    prices = []

    # 찾은 행에서 가격 정보를 추출하여 리스트에 추가
    for index, row in matching_rows.iterrows():
        price_str = row['price']
        price_num = int(price_str.replace('원', '').replace(',', '')) # '원'과 ','을 제거하기 위해 해당 문자열을 빈 문자열로 대체
        prices.append(price_num)

    # 가격 정보를 출력: 모든 가격, 평균 가격, 가장 싼 가격 출력
    if len(prices) == 0:
        Label(price_page,text="해당하는 옷 이름이 없습니다.")
    else:
        average_price = sum(prices) / len(prices)
        min_price = min(prices)
        print(f"{cloth_name}의 가격은 {prices}원이며, 평균 가격은 {average_price:,}원, 가장 싼 가격은 {min_price:,}원 입니다.") #가독성을 위해 가격 출력 시 : ,를 사용하여 천 단위로 쉼표를 출력

        # 평균 가격의 1% 범위 계산: 가격 오차 범위는 price_range 변수에 저장
        price_range = average_price * 0.01
    
        # 추천할 옷의 이름을 저장할 리스트 생성 
        recommend_clothes_similar_price = []
        for index, row in df.iterrows():
            price_str = row['price']
            price_num = int(price_str.replace('원', '').replace(',', ''))
        if abs(price_num - average_price) <= price_range and row['title'].lower() != cloth_name_lower:
            recommend_clothes_similar_price.append(row['title'])
    
    # 추천할 옷이 있다면 출력
        if len(recommend_clothes_similar_price) > 0:
           print(f"평균 가격의 1% 범위 안에 속하는 가격대의 다른 옷: {recommend_clothes_similar_price}")
        else:
          print("추천할 비슷한 가격대의 옷이 없습니다.")
        
  
    # 입력한 옷과 같은 색의 옷 추천
        cloth_colors = matching_rows['color'].str.lower().tolist()  # 입력한 옷과 같은 색깔 정보 리스트로 변환
        if len(cloth_colors) > 0:
            same_color_clothes = df.loc[(df['title'].str.lower() != cloth_name_lower) & (df['color'].str.lower().isin(cloth_colors))]  # 색깔이 같은 옷 추출

            recommend_clothes_same_color = same_color_clothes['title'].tolist()

        # 추천할 옷이 있다면 출력
            if len(recommend_clothes_same_color) > 0:
                print(f"입력한 옷과 같은 색의 옷 추천: {recommend_clothes_same_color}")
            else:
                print("추천할 같은 색의 옷이 없습니다.")
        else:
            print("입력한 옷의 색깔 정보가 없어 같은 색의 옷을 추천할 수 없습니다.")

    
    price_page.mainloop()
    


make_btn_situation =Button(root,text="클릭",command = create_price_window)
make_btn_situation.place(x=570,y=200)


root.mainloop()
