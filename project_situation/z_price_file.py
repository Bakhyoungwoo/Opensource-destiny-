import sys
from PyQt5.QtWidgets import *
import pandas as pd
from PyQt5 import uic

form_class1 = uic.loadUiType("first_window.ui")[0]
form_class4 = uic.loadUiType("price_second_window.ui")[0]
form_class5 = uic.loadUiType("price_third_window.ui")[0]


class FirstWindow(QMainWindow, form_class1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_price.clicked.connect(self.button_click_price)

    # 버튼이 클릭될 때 새로운 창 생성
    def button_click_price(self):
        self.close()
        self.price_second_window = price_SecondWindow(self)
        self.price_second_window.show()


class price_SecondWindow(QMainWindow, form_class4):
    def __init__(self, parent=None):
        super(price_SecondWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

        # 디버깅
        self.lineEdit_clothname.setText('무신사 스탠다드')

    def button_clicked(self):
        cloth_name = self.lineEdit_clothname.text()

        name_data = {'cloth_name':cloth_name}

        self.close()
        self.price_third_window = Price_ThirdWindow(name_data, self)
        self.price_third_window.show()


class Price_ThirdWindow(QMainWindow, form_class5):
    def __init__(self, name_data, parent=None):
        super(Price_ThirdWindow, self).__init__(parent)
        self.name_data = name_data
        self.setupUi(self)
        self.connect_signal_slots()
        self.text = ''
        df = pd.read_excel('example.xlsx')

        # 영어 이름의 경우 대소문자 구분 없이 옷 이름을 입력할 수 있도록 입력한 이름을 소문자로 변환
        cloth_name_lower = self.name_data['cloth_name'].lower()

        # title열에서 옷 이름이 일치하는 행을 찾음
        self.matching_rows = df.loc[df['title'].str.lower() == cloth_name_lower]

        prices = []

        for index, row in matching_rows.iterrows():
            price_str = row['price']
            price_num = int(price_str.replace('원', '').replace(',', ''))  # '원'과 ','을 제거하기 위해 해당 문자열을 빈 문자열로 대체
            prices.append(price_num)
    def connect_signal_slots(self):
        self.pushButton.clicked.connect(self.btn_show_price)
    def btn_show_price(self):
        self.label_3.setText('가격들 : ')






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    app.exec_()