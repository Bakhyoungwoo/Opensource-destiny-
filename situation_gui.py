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

photo = PhotoImage(file="gui/img2.png")

label4 = Label(root, image=photo)
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
    photo2 = PhotoImage(file="gui/codi1.png")
    label4.config(image=photo2)
    label4.place(x=220,y=60)
    #폰트 설정
    label5 = Label(root, font=('맑은 고딕',20,'bold'),text="추천된 코디 입니다.")
    label5.pack()
    
btn = Button(root, text="클릭", command=change)
btn.pack()
