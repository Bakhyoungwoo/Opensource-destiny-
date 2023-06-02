from tkinter import *
import tkinter as tk

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
    photo2 = PhotoImage(file="gui/codi1.png")
    label4.config(image=photo2)
    label4.place(x=220,y=60)
    #폰트 설정
    label5 = Label(root, font=('맑은 고딕',20,'bold'),text="추천된 코디 입니다.")
    label5.pack()
    
btn = Button(root, text="클릭", command=change)
btn.pack()
