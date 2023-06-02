from tkinter import *
import tkinter as tk


root = Tk()
root.title("사용자 코디 추천 프로그램")
root.geometry("1300x1000")

label_body = Label(root, font=('맑은 고딕',20,'bold'),text="체형 맞춤 코디")
label_body.place(x=100,y=150)

photo_body = PhotoImage()
btn_body =Button(root,text="클릭",command=select_body)
btn_body.place(x=170,y=200)

label_situation = Label(root,font=('맑은 고딕',20,'bold'),text="상황 맞춤 코디")
label_situation.place(x=500,y=150)
photo_situation = PhotoImage()
btn_situation =Button(root,text="클릭",command=select_situation)
btn_situation.place(x=570,y=200)

label_temperature= Label(root,font=('맑은 고딕',20,'bold'),text="체감 온도 맞춤 코디")
label_temperature.place(x=900,y=150)
photo_temperature = PhotoImage()
btn_temperature =Button(root,text="클릭",command=select_temperature)
btn_temperature.place(x=970,y=200)

root.mainloop()
