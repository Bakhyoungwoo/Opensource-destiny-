import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from difflib import get_close_matches
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import random


    def button_clicked(self):
        # 키와 몸무게 데이터
        X = np.array([[185, 75], [176, 65], [167, 68], [174, 65], [173, 75], [173, 73], [180, 98], [164, 59], [173, 78],
                      [185, 95], [171, 60], [170, 74], [178, 81], [170, 74], [166, 70], [189, 90], [174, 61], [180, 60],
                      [178, 69], [176, 80], [180, 73], [177, 68], [171, 67], [178, 72], [158, 48], [172, 64], [173, 61],
                      [178, 73], [173, 56], [176, 72], [187, 90], [180, 75], [175, 69], [173, 80], [165, 65], [178, 70],
                      [171, 66], [170, 64], [178, 73], [178, 74], [179, 88], [168, 64], [180, 80]])  # 입력 데이터 (키와 몸무게)
        y = np.array(
            [100, 95, 100, 100, 100, 100, 100, 95, 95, 100, 95, 105, 105, 110, 110, 115, 95, 110, 100, 110, 100, 100,
             95, 100, 95, 100, 100, 100, 95, 100, 115, 105, 100, 105, 95, 105, 95, 95, 100, 100, 110, 100,
             105])  # 출력 데이터 (옷 사이즈)
        y = y.reshape(-1, 1)
        # 선형 회귀 모델 훈련
        model = LinearRegression()
        model.fit(X, y)

        height = float(self.lineEdit_height.text())
        weight = float(self.lineEdit_weight.text())

        size = model.predict([[height, weight]])
        if 85 <= size < 90:
            output_size = 'XS'
        elif 90 <= size < 95:
            output_size = 'S'
        elif 95 <= size < 100:
            output_size = 'M'
        elif 100 <= size < 105:
            output_size = 'L'
        elif 105 <= size < 110:
            output_size = 'XL'
        elif 110 <= size < 115:
            output_size = 'XXL'
        else:
            output_size = '사이즈를 결정할 수 없습니다.'

        # 결과 출력
        self.label_size_result.setText("예상 옷 사이즈는 {}입니다.".format(output_size))
        self.pixmap = QPixmap('koreasize.PNG')
        self.label_size_image.setPixmap(
            QPixmap(self.pixmap).scaled(self.label_size_image.width(), self.label_size_image.height(),
                                        Qt.IgnoreAspectRatio))
        self.label_size_image.resize(700, 230)


class Situation_SecondWindow(QMainWindow, form_class2):
    def __init__(self, parent=None):
        super(Situation_SecondWindow, self).__init__(parent)
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
        self.situation_third_window = Situation_ThirdWindow(data, self)
        self.situation_third_window.show()


def get_similar_words(word, words_list):
    # 문자열 타입의 값만 words_list에 추가
    words_list = [str(w) for w in words_list]
    return get_close_matches(word, words_list, n=1, cutoff=0.8)


class Situation_ThirdWindow(QMainWindow, form_class3):
    def __init__(self, data, parent=None):
        super(Situation_ThirdWindow, self).__init__(parent)
        self.data = data
        self.setupUi(self)
        self.connect_signal_slots()
        self.text = ''

        df = pd.read_excel('Excel_data/codi_data.xlsx')
        #딕셔너리 추출은 self.data['sex']
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
            # 일치하는 코디가 없다는 문구와 겹침으로 삭제
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
                # 코디 이미지 표시
                pixamp = QPixmap('codi/{}.png'.format(random_outfit))
                self.label_codi_reference.setPixmap(
                    QPixmap(pixamp).scaled(self.label_codi_reference.width(), self.label_codi_reference.height(),
                                           Qt.IgnoreAspectRatio))
                self.label_codi_reference.resize(500, 570)

            # 중복되지 않는 코디가 없다면 모든 코디가 추천 리스트에 이미 추가되었다는 뜻이므로 종료
            else:
                self.text += '더 이상 추천할 코디가 없습니다.\n'
                self.label.setText(self.text)



class Price_SecondWindow(QMainWindow, form_class4):
    def __init__(self, parent=None):
        super(Price_SecondWindow, self).__init__(parent)
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
        #상의 인지 하의 인지를 선택하는 기능이 필요.
        self.df = pd.read_excel('Excel_data/cloth.xlsx')  # 인스턴스 변수로 만들기

    def connect_signal_slots(self):
        self.pushButton.clicked.connect(self.btn_show_price)

    def btn_show_price(self):
        self.prices = []  # 인스턴스 변수 self.price를 빈 목록으로 초기화합니다

        cloth_name_lower = self.name_data['cloth_name'].lower()  # cloth_name_lower 인스턴스 변수 만들기

        matching_rows = self.df.loc[self.df['title'].str.lower() == cloth_name_lower]


        for index, row in matching_rows.iterrows():
            price_str = row['price']
            price_num = int(price_str.replace('원', '').replace(',', ''))
            self.prices.append(price_num)  # 추출된 가격을 self.price에 추가합니다

        if len(self.prices) == 0:
            self.label_empty.setText("해당하는 옷 이름이 없습니다.")
        # 유니섹스 세미 와이드 밴딩 슬랙스
        else:
            self.average_price = sum(self.prices) / len(self.prices)
            self.min_price = min(self.prices)
            self.label_prices.setText('가격 : ')
            self.text += '\n'.join(['{}원'.format(price) for price in self.prices])
            self.label_6.setText(self.text)
            self.label_average_min.setText('평균가격과 제일 싼 가격')
            self.label_averageprice.setText('평균가격은 : {0} \n 제일 싼 가격은 : {1}'.format(self.average_price, self.min_price))

            pixamp = QPixmap('cloth/{}.png'.format(cloth_name_lower))
            self.label_price_reference.setPixmap(
                QPixmap(pixamp).scaled(self.label_price_reference.width(), self.label_price_reference.height(),
                                       Qt.IgnoreAspectRatio))
            self.label_price_reference.resize(550, 560)


            cloth_colors = matching_rows['color'].str.lower().tolist()  # 입력한 옷과 같은 색깔 정보 리스트로 변환
            if len(cloth_colors) > 0:
                same_color_clothes = self.df.loc[(self.df['title'].str.lower() != cloth_name_lower) & (
                    self.df['color'].str.lower().isin(cloth_colors))]  # 색깔이 같은 옷 추출

                recommend_clothes_same_color = same_color_clothes['title'].tolist()

                if len(recommend_clothes_same_color) > 0:
                    recommend_clothes_text = '\n'.join(recommend_clothes_same_color)
                    self.label_recommend_color.setText(f"입력한 옷과 같은 색의 옷 추천:\n\n{recommend_clothes_text}")
                else:
                    self.label_recommend_color.setText("추천할 같은 색의 옷이 없습니다.")
            else:
                self.label_recommend_color.setText("입력한 옷의 색깔 정보가 없어 같은 색의 옷을 추천할 수 없습니다.")



class Color_SecondWindow(QMainWindow, form_class6):
    def __init__(self, parent=None):
        super(Color_SecondWindow, self).__init__(parent)
        self.setupUi(self)
        self.connect_signal_slots_top()
        self.connect_signal_slots_bottom()
        self.btn_result()
        self.shirts_data = pd.read_excel('Excel_data/shirts.xlsx')
        self.pants_data = pd.read_excel('Excel_data/pants.xlsx')

        self.pixmap = QPixmap('color_combinate.PNG')
        self.label_color_combinate.setPixmap(
            QPixmap(self.pixmap).scaled(self.label_color_combinate.width(), self.label_color_combinate.height(),
                                        Qt.IgnoreAspectRatio))
        self.label_color_combinate.resize(560, 520)

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
        # 호환성 수준이 다른 색 조합 사전
        best_color_combinations = {
            '빨강': ['진청', '검정'],
            '핑크': ['흰색'],
            '노랑': ['검정'],
            '초록': ['진청', '검정'],
            '파랑': ['흰색'],
            '남색': ['흰색'],
            '흰색': ['연청', '진청'],
            '검정': ['연청', '베이지']
        }
        good_color_combinations = {
            '빨강': ['회색'],
            '핑크': ['회색', '연청', '검정'],
            '노랑': ['회색', '진청'],
            '초록': ['회색', '베이지'],
            '파랑': ['회색', '베이지'],
            '남색': ['회색', '검정', '베이지'],
            '흰색': ['회색', '검정'],
            '검정': ['회색', '진청', '검정']
        }
        not_bad_color_combinations = {
            '빨강': ['흰색'],
            '핑크': ['베이지'],
            '노랑': [],
            '초록': ['연청', '흰색'],
            '파랑': [],
            '남색': ['연청'],
            '흰색': ['베이지'],
            '검정': ['흰색']
        }
        worst_color_combinations = {
            '빨강': ['연청', '베이지'],
            '핑크': [],
            '노랑': ['연청', '베이지', '흰색'],
            '초록': [],
            '파랑': ['연청', '진청', '베이지'],
            '남색': [],
            '흰색': ['흰색'],
            '검정': []
        }

        if self.shirt_color == self.pants_color:
            self.label_result.setText("상의와 하의의 색상이 일치합니다. \n평범하지만 괜찮은, 무난한 조합입니다!")
        else:
            shirt_color = self.shirt_color[0] if self.shirt_color else None
            pants_color = self.pants_color[0] if self.pants_color else None
            # 색의 조합 결과 에 따라 문구 출력

            if shirt_color in best_color_combinations.get(pants_color, []):
                self.label_result.setText(f"상의와 하의의 색상 조합이 잘 어울립니다! ({shirt_color}, {pants_color})")
            elif shirt_color in good_color_combinations.get(pants_color, []):
                self.label_result.setText(f"상의와 하의의 색상 조합이 어느 정도 어울립니다! ({shirt_color}, {pants_color})")
            elif shirt_color in not_bad_color_combinations.get(pants_color, []):
                self.label_result.setText(
                    f"상의와 하의의 색상 조합이 나쁘진 않지만, 더 좋은 조합을 찾아보는 것은 어떨까요? ({shirt_color}, {pants_color})")
            elif shirt_color in worst_color_combinations.get(pants_color, []):
                self.label_result.setText(
                    f"어우! 이건 좀 아닌 것 같습니다! 새로운 시도를 해보는 게 아니라면, 다른 색깔의 조합을 고려해 보세요. ({shirt_color}, {pants_color})")
            else:
                self.label_result.setText(f"저희 색 조합 데이터에는 없는 조합입니다.\n 흐음... 당신의 조합이 괜찮기를 바랍니다!")

#윈도우창 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_total = total_window()
    window_total.show()

    sys.exit(app.exec_())