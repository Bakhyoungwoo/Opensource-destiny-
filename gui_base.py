from tkinter import *
import tkinter as tk

global sexual
global codi_situation

root = Tk()
root.title("Nado GUI")
root.geometry("1000x1000")

label1 = Label(root, text="man or woman",)
#pack() 은 절댓값으로 위치 고정
label1.pack()

#entry 는 1줄 입력에 좋음.
sex = Entry(root, width = 20)
sex. pack()
sex.insert(0, "man or woman")


#입력한 값을 sexual 이란 변수에 저장하는 버튼
def btnsave_sexual():
    
    #입력한 성별을 sexual이랑 변수에 저장
    sexual= sex.get()
    print(sexual)
    
btn1 = Button(root, text="click", command= btnsave_sexual)
btn1.place(x=600,y=20)



label2 = Label(root, text="what kind of situation")
label2.pack()

situation = Entry(root, width = 20)
situation.pack()
situation.insert(0, "situation")

def btnsave_situation():
    # 1 : 첫번째 라인, 0 : 0번째 colum 위치
    
    #입력한 성별을 sexual이랑 변수에 저장
    codi_situation = situation.get()
    print(codi_situation)
    
btn2 = Button(root, text="click", command= btnsave_situation)
btn2.place(x=600,y=60)

label3 = Label(root, text="what kind of codi")
label3.pack()

#entry 생성
codi = Entry(root, width = 20)
codi.pack()
codi.insert(0, "codi")

def btnsave_codi():
    # 1 : 첫번째 라인, 0 : 0번째 colum 위치
    
    #입력한 성별을 sexual이랑 변수에 저장
    codi_reference = codi.get()
    print(codi_reference)
    
btn3 = Button(root, text="click", command= btnsave_codi)
btn3.place(x=600,y=100)

