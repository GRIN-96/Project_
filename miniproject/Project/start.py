
# -- coding: utf-8 --

import sys

from PyQt5 import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from test import Ui_MainWindow
from sec import Ui_Form
import time
import urllib.request
import os
import requests
import subprocess
import re
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import subprocess
from webdriver_manager.chrome import ChromeDriverManager
import ctypes

#python GUI 툴킷
from tkinter import *

# 파일 불러오는 함수 생성
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#################test.ui 가져오기#######################
form = resource_path('test.ui')
form_class = uic.loadUiType(form)[0]
#################sec.ui 가져오기########################
form_second = resource_path('sec.ui')
form_secondwindow = uic.loadUiType(form_second)[0]
#################thrd.ui 가져오기########################
form_thrd = resource_path('thrd.ui')
form_thrdwindow = uic.loadUiType(form_thrd)[0]
######################################################



class auto_w(QMainWindow,form_class): #class name 변경
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        # startButton 클릭시 autoExcute 함수 수행
        self.pushButton.clicked.connect(self.man_hair)
        self.pushButton_2.clicked.connect(self.girl_hair)

        # button 클릭시 함수 수행
        self.pushButton_3.clicked.connect(self.fileopen)

    def man_hair(self):
        self.hide()  # 메인윈도우 숨김
        self.second = NewWindw()
        self.second.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.show()

    def girl_hair(self):
        self.hide()  # 메인윈도우 숨김
        self.thrd = NewWindw1()
        self.thrd.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.show()


    def fileopen(self):
        global filename
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')



class NewWindw(QDialog,QWidget,form_secondwindow):
    def __init__(self):
        super(NewWindw, self).__init__()
        self.initUi()
        self.show()

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)

    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.



class NewWindw1(QDialog,QWidget,form_thrdwindow):
    def __init__(self):
        super(NewWindw1, self).__init__()
        self.initUi()
        self.show()

        # 이벤트 함수 조건
        self.pushButton_2.clicked.connect(self.btn_second_to_main)

    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.




if __name__ == "__main__":
    app =QApplication(sys.argv)
    main_dialog = auto_w() #해당부분 위 class name과 동일하게 작성
    main_dialog.show()
    QApplication.processEvents()
    app.exit(app.exec_())
    app.exec_()

