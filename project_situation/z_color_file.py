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
        # Color combination dictionaries with different levels of compatibility
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
            self.label_result.setText("상의와 하의의 색상이 일치합니다. 평범하지만 괜찮은, 무난한 조합입니다!")
        else:
            shirt_color = self.shirt_color[0] if self.shirt_color else None
            pants_color = self.pants_color[0] if self.pants_color else None
        
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




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Color_FirstWindow()
    window.show()
    app.exec_()                      