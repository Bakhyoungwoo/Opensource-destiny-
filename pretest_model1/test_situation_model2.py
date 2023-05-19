from tkinter import *
import tkinter as tk
import pandas as pd
from difflib import get_close_matches
from PIL import Image, ImageTk
import os
import random
from openpyxl import *


root = Tk()
root.title("의류 추천 프로그램")
root.geometry("1300x1000")


label_situation = Label(root,font=('맑은 고딕',20,'bold'),text="상황 맞춤 코디")
label_situation.place(x=500,y=150)
photo_situation = PhotoImage()

global words_list
try:
    # 엑셀 파일 로드
    df = pd.read_excel('codi_data.xlsx')
except FileNotFoundError:
    print("열고자 하는 엑셀 파일이 존재하지 않습니다.")
    exit()

def create_situation_window():
    app=Tk()
    app.title("test1")
    app.geometry("1300x1000")
    

    # 사용자로부터 정보 입력 받기
    label_sex = Label(app,text="성별이 어떻게 되시나요? : ")
    label_sex.pack()
    situation_sex = Entry(app, width = 20)
    situation_sex.pack()
    situation_sex.insert(0, "ex : 남성 or 여성")
    
    # current color 변수에 색깔 값 저장
    def btnsave_situation_sex():
        #전역변수 설정
        global current_sex
        current_sex = situation_sex.get()
        print(current_sex)
    
    btn_sex = Button(app, text="click", command=btnsave_situation_sex)
    btn_sex.place(x=900,y=20)
    
    # 상황 데이터
    label_situation = Label(app,text="어떤 상황에서 입을 옷을 추천받고 싶으세요?: ")
    label_situation.pack()
    situation = Entry(app, width = 20)
    situation.pack()
    situation.insert(0, "ex : 결혼식")
 
    def btnsave_situation():
        #전역변수 설정
        global current_situation
        current_situation = situation.get()
        print(current_situation)
    # 버튼 설정
    btn_situation = Button(app, text="click", command=btnsave_situation)
    btn_situation.place(x=900,y=60)
    # 색깔 데이터
    label_color = Label(app,text="어떤 색의 옷을 추천받고 싶으세요?(상의) : ")
    label_color.pack()
    situation_color = Entry(app, width = 20)
    situation_color.pack()
    situation_color.insert(0, "ex : 파란색")
    
    # current color 변수에 색깔 값 저장
    def btnsave_situation_color():
        #전역변수 설정
        global current_color
        current_color = situation_color.get()
        print(current_color)
    
    btn_color = Button(app, text="click", command=btnsave_situation_color)
    btn_color.place(x=900,y=100)
    
    # 유사한 단어 찾기 함수 정의
    def get_similar_words(word, words_list):
        # 문자열 타입의 값만 words_list에 추가
        words_list = [str(w) for w in words_list]
        return get_close_matches(word, words_list, n=1, cutoff=0.8)
    

# 추천된 코디를 저장하는 리스트
    recommended_outfits = []
    
    def create_recommendpage():
        app2=Tk()
        app2.title("test_page")
        app2.geometry("1300x1000")
        
        while True:
        # 입력받은 정보와 유사한 데이터 추출
            filtered_df = df[df['gender'].str.contains('|'.join(get_similar_words(current_sex, df['gender'])), na=False)]
            filtered_df = filtered_df[df['codi'].str.contains('|'.join(get_similar_words(current_situation, df['codi'])), na=False)]
            filtered_df = filtered_df[filtered_df['color'].str.contains('|'.join(get_similar_words(current_color, df['color'])), na=False)]
        
        
            # 추천할 옷 선택
            if filtered_df.empty:
                label_empty = Label(app2,text="일치하는 코디가 없습니다.")
                label_empty.pack()
                break
            else:
            # 추천 데이터에서 중복되지 않게 선택하기 위해
            # 추천된 코디 리스트와 비교하여 중복되지 않는 코디만 추천 리스트에 추가
                unique_outfits = []
            
                for outfit in filtered_df['title'].tolist():
                    if outfit not in recommended_outfits:
                        unique_outfits.append(outfit)

                # 중복되지 않는 코디가 있다면 추천 리스트에서 랜덤으로 선택하고, 기존 추천 리스트에 추가
                if unique_outfits:
                    random_outfit = random.choice(unique_outfits)
                    recommended_outfits.append(random_outfit)
                    label_recommend = Label(app2, text = "추천되는 코디:")
                    label_recommend.pack()
                    label_outfit = Label(app2 , text = random_outfit)
                    label_outfit.pack()
                    print(random_outfit)
                # 중복되지 않는 코디가 없다면 모든 코디가 추천 리스트에 이미 추가되었다는 뜻이므로 종료
                # 현재 추천할 코디가 없을 경우 이 문구가 바로 뜸
                else:
                    label_done = Label(app2 , text="더 이상 추천할 코디가 없습니다.")
                    label_done.pack()
                    break
            
                #사용자의 답변 받기
                label_answer = Label(app2,text = "추천된 코디가 마음에 드나요? ")  
                label_answer.pack()  
                #Entry 설정
                situation_answer = Entry(app2, width = 20)
                situation_answer.pack()
                situation_answer.insert(0, "ex : 파란색")
                height = 60
            
                def btnsave_situation_answer():
                    global current_answer
                    current_answer = situation_answer.get()
                    print(current_answer)
    
                btn_sit_answer = Button(app2, text="click", command=btnsave_situation_answer)
                btn_sit_answer.place(x=900,y=100)
            
                def answer():    
                    #대답이 예일 경우(answer = 예)
                    if answer == '예':
                        label_perfect = Label(app2, text="좋아요! 코디가 마음에 드셨다니 다행입니다!")
                        label_perfect.pack()
                    #대답이 아니오 일 경우(answer = 아니오)
                    elif answer == '아니오':
                        print("Hello")
                        label_no = Label(app2, text="다른 코디를 추천해드릴게요!")
                        label_no.pack()
                    
                #answer함수 실행시키는 버튼
                btn_answer = Button(app2, text="click", command=answer)
                btn_answer.place(x=900, y=60)
            
        app2.mainloop()
        
    btn_change = Button(app, text="click", command=create_recommendpage)
    btn_change.place(x=900,y=150)
    
    #이미지 예시
    photo_example = ImageTk.PhotoImage(file="pretest_model1/img.png")

    # Resize the image
    img = Image.open("pretest_model1/img.png")
    img_resize = img.resize((256, 256))
    photo_resized = ImageTk.PhotoImage(img_resize)
    btn_photo = Button(app, image = photo_example)
    btn_photo.place(x=900,y=210)

    
    app.mainloop()
    


make_btn_situation =Button(root,text="클릭",command = create_situation_window)
make_btn_situation.place(x=570,y=200)


root.mainloop()
