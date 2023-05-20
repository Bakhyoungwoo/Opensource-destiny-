import sys
from PyQt5.QtWidgets import *
from difflib import get_close_matches
import pandas as pd
from PyQt5 import uic
import random

form_class1 = uic.loadUiType("first_window.ui")[0]
form_class2 = uic.loadUiType("second_window.ui")[0]
form_class3 = uic.loadUiType("third_window.ui")[0]


class FirstWindow(QMainWindow, form_class1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    # 버튼이 클릭될 때 새로운 창 생성
    def button_clicked(self):
        self.close()
        self.second_window = SecondWindow(self)
        self.second_window.show()


class SecondWindow(QMainWindow, form_class2):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

        # 디버깅
        self.lineEdit_sex.setText('남성')
        self.lineEdit_recommend.setText('데이트')
        self.lineEdit_color.setText('회색')

    def button_clicked(self):
        sex = self.lineEdit_sex.text()
        recommend = self.lineEdit_recommend.text()
        color = self.lineEdit_color.text()

        data = {'sex': sex, 'recommend': recommend, 'color': color}

        self.close()
        self.third_window = ThirdWindow(data, self)
        self.third_window.show()


def get_similar_words(word, words_list):
    # 문자열 타입의 값만 words_list에 추가
    words_list = [str(w) for w in words_list]
    return get_close_matches(word, words_list, n=1, cutoff=0.8)


class ThirdWindow(QMainWindow, form_class3):
    def __init__(self, data, parent=None):
        super(ThirdWindow, self).__init__(parent)
        self.data = data
        self.setupUi(self)
        self.connect_signal_slots()
        self.text = ''

        df = pd.read_excel('codi_data.xlsx')

        filtered_df = df[
            df['gender'].str.contains('|'.join(get_similar_words(self.data['sex'], df['gender'])), na=False)]
        filtered_df = filtered_df[
            df['codi'].str.contains('|'.join(get_similar_words(self.data['recommend'], df['codi'])), na=False)]
        self.filtered_df = filtered_df[
            filtered_df['color'].str.contains('|'.join(get_similar_words(self.data['color'], df['color'])), na=False)]

        self.recommended_outfits = list()

        self.recommend_clothes()

    def connect_signal_slots(self):
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        if self.radioButton_yes.isChecked():
            self.label2.setText('좋아요! 코디가 마음에 드셨다니 다행입니다!')

        else:
            self.label2.setText('다른 코디를 추천해드릴게요!')
            self.recommend_clothes()

    def recommend_clothes(self):

        if self.filtered_df.empty:
            self.label.setText('일치하는 코디가 없습니다.')
        else:
            unique_outfits = []

            for outfit in self.filtered_df['title'].tolist():
                if outfit not in self.recommended_outfits:
                    unique_outfits.append(outfit)

            if unique_outfits:
                random_outfit = random.choice(unique_outfits)
                self.recommended_outfits.append(random_outfit)
                self.text += '추천되는 코디 : {}\n'.format(random_outfit)
                self.label.setText(self.text)
            # 중복되지 않는 코디가 없다면 모든 코디가 추천 리스트에 이미 추가되었다는 뜻이므로 종료
            else:
                self.text += '더 이상 추천할 코디가 없습니다.\n'
                self.label.setText(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    app.exec_()