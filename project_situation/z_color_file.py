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
