import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pandas as pd
from PyQt5 import uic

form_class1 = uic.loadUiType("first_window.ui")[0]
form_class6 = uic.loadUiType("color_second_window.ui")[0]

class Color_FirstWindow(QMainWindow, form_class1):
    def __init__(self):
        super().__init__(parent=None)
        self.setupUi(self)
        self.pushButton_color.clicked.connect(self.button_click_color)
    # 버튼이 클릭될 때 새로운 창 생성
    def button_click_color(self):
        self.close()
        self.color_second_window = Color_SecondWindow(self)
        self.color_second_window.show()
        
class Color_SecondWindow(QMainWindow, form_class6):
    def __init__(self, parent=None):
        super(Color_SecondWindow, self).__init__(parent)        
        self.setupUi(self)
        self.connect_signal_slots_top()
        self.connect_signal_slots_bottom()
        self.btn_result()
        self.shirts_data = pd.read_excel('shirts.xlsx')
        self.pants_data = pd.read_excel('pants.xlsx')
        self.pixmap = QPixmap('color_combinate.PNG')
        self.label_color_combinate.setPixmap(QPixmap(self.pixmap).scaled(self.label_color_combinate.width(), self.label_color_combinate.height(),Qt.IgnoreAspectRatio))
        self.label_color_combinate.resize(400, 390)
        
    def connect_signal_slots_top(self):
        self.pushButton_top.clicked.connect(self.btn_top_color)

    def btn_top_color(self):
        shirt_name = self.lineEdit_third_topname.text()
        # 상의 예시 : 에센셜 쿨 코튼 2-PACK 티셔츠 블랙

        self.shirt_color = self.shirts_data.loc[self.shirts_data['title'] == shirt_name, 'color'].values
        if self.shirt_color:
            self.label_top_color.setText(f"{shirt_name}의 \n색상정보 : {self.shirt_color[0]}")
        else:
            self.label_top_color.setText(f"{shirt_name}에 대한 정보를 찾을 수 없습니다.")

    def connect_signal_slots_bottom(self):
        self.pushButton_bottom.clicked.connect(self.btn_bottom_color)

    def btn_bottom_color(self):
        pants_name = self.lineEdit_third_bottomname.text()
        # 하의 예시: 유니섹스 세미 와이드 밴딩 슬랙스

        self.pants_color = self.pants_data.loc[self.pants_data['title'] == pants_name, 'color'].values
        if self.pants_color:
            self.label_bottom_color.setText(f"{pants_name}의 \n색상정보 : {self.pants_color[0]}")
        else:
            self.label_bottom_color.setText(f"{pants_name}에 대한 정보를 찾을 수 없습니다.")  
 
    def btn_result(self):
        self.pushButton_result.clicked.connect(self.tell_result_color)

    def tell_result_color(self):
        pixmap = QPixmap('pythonProject2/color_combinate.PNG')
        self.label_color_combinate = QLabel(self)

        self.label_color_combinate.setPixmap(pixmap)
        self.label_color_combinate.resize(pixmap.width(), pixmap.height())                  
                      