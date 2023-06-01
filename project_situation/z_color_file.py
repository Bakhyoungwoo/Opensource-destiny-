import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pandas as pd
from PyQt5 import uic

form_class1 = uic.loadUiType("first_window.ui")[0]

class Color_FirstWindow(QMainWindow, form_class1):
    def __init__(self):
        super().__init__(parent=None)
        self.setupUi(self)
        self.pushButton_color.clicked.connect(self.button_click_color)
