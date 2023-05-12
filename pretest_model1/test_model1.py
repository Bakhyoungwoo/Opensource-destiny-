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
    
    label1 = Label(app, text="man or woman",)
    #pack() 은 절댓값으로 위치 고정
    label1.pack()

    #entry 는 1줄 입력에 좋음.
    sex = Entry(app, width = 20)
    sex. pack()
    sex.insert(0, "man or woman")


    #입력한 값을 sexual 이란 변수에 저장하는 버튼
    def btnsave_sexual():
    
    #입력한 성별을 sexual이랑 변수에 저장
        sexual= sex.get()
        print(sexual)
    
    btn1 = Button(app, text="click", command= btnsave_sexual)
    btn1.place(x=900,y=20)



    label2 = Label(app, text="what kind of situation")
    label2.pack()

    situation = Entry(app, width = 20)
    situation.pack()
    situation.insert(0, "situation")

    def btnsave_situation():
        # 1 : 첫번째 라인, 0 : 0번째 colum 위치
    
       #입력한 성별을 sexual이랑 변수에 저장
        codi_situation = situation.get()
        print(codi_situation)
    
    btn2 = Button(app, text="click", command= btnsave_situation)
    btn2.place(x=900,y=60)

    label3 = Label(app, text="what kind of codi")
    label3.pack()

    #entry 생성
    codi = Entry(app, width = 20)
    codi.pack()
    codi.insert(0, "codi")

    def btnsave_codi():
        # 1 : 첫번째 라인, 0 : 0번째 colum 위치

        #입력한 성별을 sexual이랑 변수에 저장
        codi_reference = codi.get()
        print(codi_reference)
    
    btn3 = Button(app, text="click", command= btnsave_codi)
    btn3.place(x=900,y=100)
    
    
    
    photo = PhotoImage(file="pretest_model1/img.png")

    label4 = Label(app, text="done")
    label4.pack()

    def change():
   
       #라벨 삭제
        label1.pack_forget()
       #entry 삭제
        sex.pack_forget()
      #버튼 삭제
        btn1.destroy()
    
        label2.pack_forget()
        situation.pack_forget()
        btn2.destroy()
    
        label3.pack_forget()
        codi.pack_forget()
        btn3.destroy()
    
    
        btn.pack_forget()
    
        global photo2
        photo2 = PhotoImage(file="pretest_model1/1.png")
        label4.config(image=photo2)
        label4.place(x=220,y=60)
        #폰트 설정
        label5 = Label(app, font=('맑은 고딕',20,'bold'),text="추천된 코디 입니다.")
        label5.pack()
    
    btn = Button(app, text="클릭", command=change)
    btn.pack()
    
    app.mainloop()
    


make_btn_situation =Button(root,text="클릭",command = create_situation_window)
make_btn_situation.place(x=570,y=200)


root.mainloop()
