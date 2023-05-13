from tkinter import *
import tkinter as tk
import pandas as pd
from difflib import get_close_matches
import random



root = Tk()
root.title("의류 추천 프로그램")
root.geometry("1300x1000")


label_situation = Label(root,font=('맑은 고딕',20,'bold'),text="상황 맞춤 코디")
label_situation.place(x=500,y=150)
photo_situation = PhotoImage()

def create_situation_window():
    app=Tk()
    app.title("test1")
    app.geometry("1300x1000")
    

    # 사용자로부터 정보 입력 받기
    # 상황 데이터
    label_situation = Label(app,text="어떤 상황에서 입을 옷을 추천받고 싶으세요?: ")
    label_situation.pack()
    situation = Entry(app, width = 20)
    situation.pack()
    situation.insert(0, "ex : wedding")
 
    def btnsave_situation():
        #전역변수 설정
        global current_situation
        current_situation = situation.get()
        print(current_situation)
    
    btn1 = Button(app, text="click", command=btnsave_situation)
    btn1.place(x=900,y=20)
    current_color = input("어떤 색깔의 옷을 추천받고 싶으세요?: ")

    # 유사한 단어 찾기 함수 정의
    def get_similar_words(word, words_list):
        # 문자열 타입의 값만 words_list에 추가
        words_list = [str(w) for w in words_list]
        return get_close_matches(word, words_list, n=1, cutoff=0.8)

# 추천된 코디를 저장하는 리스트
    recommended_outfits = []
    try:
    # 엑셀 파일 로드
        df = pd.read_excel('codi_data.xlsx')
    except FileNotFoundError:
        exit()

    while True:
        # 입력받은 정보와 유사한 데이터 추출
        filtered_df = df[df['codi'].str.contains('|'.join(get_similar_words(current_situation, df['codi'])), na=False)]
        filtered_df = filtered_df[df['color'].str.contains('|'.join(get_similar_words(current_color, df['color'])), na=False)]

        # 추천할 옷 선택
        if filtered_df.empty:
            print("일치하는 코디가 없습니다.")
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
                print("추천되는 코디:")
                print(random_outfit)
            # 중복되지 않는 코디가 없다면 모든 코디가 추천 리스트에 이미 추가되었다는 뜻이므로 종료
            else:
                print("더 이상 추천할 코디가 없습니다.")
                break

    # 사용자의 답변 받기
        answer = input("추천된 코디가 마음에 드나요? (예/아니오): ")
        if answer.lower() == '예':
            print("좋아요! 코디가 마음에 드셨다니 다행입니다!")
            break
        elif answer.lower() == '아니오':
            print("다른 코디를 추천해드릴게요!")
            continue
        else:
            print("예 또는 아니오로 대답해주세요.")
    
    app.mainloop()
    


make_btn_situation =Button(root,text="클릭",command = create_situation_window)
make_btn_situation.place(x=570,y=200)


root.mainloop()
