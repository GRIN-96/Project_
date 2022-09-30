import sys
from PyQt5.QtWidgets import *
import PyQt5
import os
from PyQt5 import QtWidgets, uic, QtGui,QtCore
import random
import PIL
from PIL import Image
import pandas as pd
import numpy as np
import dload
import bs4
from bs4 import BeautifulSoup
import urllib.request
import requests
import pygame
import json
import glob
from glob import glob
import cv2
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
import PySide2
from PySide2.QtWidgets import QMessageBox
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='maple.mysql.database.azure.com', user='maple', password='password',
                      db='project', charset='utf8', port=3306,
                      autocommit=True, cursorclass=pymysql.cursors.DictCursor)

# 파일 불러오는 함수 생성
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#################test.ui 가져오기#######################
form_class = uic.loadUiType("Ui/test.ui")[0]
#################sec.ui 가져오기########################
form_secondwindow = uic.loadUiType("Ui/sec.ui")[0]
#################thrd.ui 가져오기########################
form_thrdwindow = uic.loadUiType("Ui/thrd.ui")[0]
###############man_hair.ui 가져오기#####################
form_hair = uic.loadUiType("Ui/man_hair.ui")[0]
###############girl_hair.ui 가져오기#####################
form_hair1 = uic.loadUiType("Ui/girl_hair.ui")[0]
###############final_page.ui 가져오기#####################
form_final = uic.loadUiType("Ui/final_page.ui")[0]
################last_page.ui 가져오기#####################
form_last = uic.loadUiType("Ui/last_page.ui")[0]
##################output.ui 가져오기#####################
form_output = uic.loadUiType("Ui/output.ui")[0]
#######################################################


class auto_w(QMainWindow,form_class): #class name 변경
    def __init__(self):
        global input_p, name, fname1, face
        face = 21078
        fname1 = 0
        name = 0
        input_p = 0
        super().__init__()
        self.setupUi(self)

        # self.playsound.playsound('bgm.mp3')

        pygame.mixer.init()
        pygame.mixer.music.load('bgm.mp3')
        pygame.mixer.music.play()
        self.label_2.setStyleSheet(f"border-image:url(\'MaplePicture/i15523914217.jpg\');")


        # startButton 클릭시 autoExcute 함수 수행
        self.pushButton.clicked.connect(self.man_hair)
        self.pushButton_2.clicked.connect(self.girl_hair)
        self.pushButton_4.clicked.connect(self.names)
        self.lineEdit_2.returnPressed.connect(self.names)
        # button 클릭시 함수 수행
        self.pushButton_3.clicked.connect(self.fileopen)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


    def man_hair(self):
        self.hide()  # 메인윈도우 숨김
        self.second = NewWindw_01()
        self.second.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.show()
        # 헤어 월드컵 우승 text 가져오기
        # self.label_5.setText(f_img)

    def girl_hair(self):
        self.hide()  # 메인윈도우 숨김
        self.thrd = NewWindw_02()
        self.thrd.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.show()


    def fileopen(self):
        global input_p,fname1
        fname1 = QFileDialog.getOpenFileName(self)
        input_p = fname1[0]
        self.graphicsView.setStyleSheet(f"border-image:url(\'{input_p}\');")


    def names(self):
        global name
        # 파일이 있는경우 삭제 하는 함수
        file_path = f"{3}.jpg"

        if os.path.exists(file_path):
            os.remove(file_path)

        # 메이플 지지에서 캐릭터 정보를 가져오는 함수.
        Nickname = []
        name = self.lineEdit_2.text()
        url = f'https://maple.gg/u/{name}'
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            img = soup.find_all("div", class_="col-6 col-md-8 col-lg-6")
            for i in img:
                Nickname.append(i.find('img')['src'])
            img = Nickname[0]
            dload.save(img, f'{3}.jpg')
            self.graphicsView_2.setStyleSheet(f"border-image:url(\'3.jpg\');")


        global input_p
        input_p = '3.jpg'




###############################################남성 헤어 월드컵 #######################################

class NewWindw_01(QDialog,QWidget,form_hair):
    def __init__(self):
        super(NewWindw_01, self).__init__()
        self.setupUi(self)
        self.show()



        self.graphicsView_2.setStyleSheet(f"border-image:url(\'MaplePicture/pokemon.png\');")
        print(input_p)
        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)
        # 콤보박스에서 목록 선택 시 이벤트 발생
        self.comboBox.currentIndexChanged.connect(self.printShtname)
        # 월드컵 실행창 활성화
        self.pushButton_2.clicked.connect(self.worldcup)

        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.

    def worldcup(self):
        self.hide()  # 메인윈도우 숨김
        self.sec = NewWindw()
        self.sec.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.

    # 콤보박스의 내용 변경시 터미널에 시트명 출력
    def printShtname(self):
        global play
        play = self.comboBox.currentText()



class NewWindw(QDialog,QWidget,form_secondwindow):
    def __init__(self):
        super(NewWindw, self).__init__()
        self.setupUi(self)
        self.show()


        self.graphicsView.setStyleSheet(f"border-image:url(\'MaplePicture/pokemon.png\');")
        self.graphicsView_2.setStyleSheet(f"border-image:url(\'MaplePicture/map1.jpg\');")

        # 월드컵 시작
        self.WorldCup()
        global round
        round = rounds
        self.select_items()

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.


    def WorldCup(self):
        global c1, c2, filenamelist, c4, c8, c16, c32, c0, c_cup, fname, face
        filenamelist = os.listdir('Man_hair')
        c1 = []  # 승자
        c2 = []  # 2강
        c4 = []  # 4강
        c8 = []  # 8강
        c16 = []  # 16강
        c32 = []  # 32강
        c0 = []  # 처음에 사용자가 입력한 round에 따른 초기화 값을 저정함.
        c_cup = {1: c1, 2: c2, 4: c4, 8: c8, 16: c16, 32: c32}
        fname = []  # 파일이름
        face = 21045
        for filenames in filenamelist:
            fname.append(filenames)
            random.shuffle(fname)


        # 라운드 셋팅
        global rounds

        # 선택값으로 초기화하기
        rounds = int(play[:-1]) # 2,4,8,16 ...
        for i in range(rounds):
            c0.append(i)
        c_cup[rounds] = c0  # 초기화한 값



        # 게임을 수행하는 부분.
    def select_items(self):  # round로 올 수 있는 값 : 64/32/16/8/4/2
        global get_name
        get_name = lambda x: x.split('.')[0]  # 파일명만 가져오도록 하는 간단한 함수.
        global j
        print(c_cup)

        j=0
        self.select_items2(round)


    def select_items2(self,round):

        global img1,img2,j



        self.lineEdit_2.setText(f'{round}강 {int((j + 2) / 2)}/{int(round / 2)}')
        img1 = get_name(fname[c_cup[round][j]])
        img2 = get_name(fname[c_cup[round][j + 1]])
        self.lineEdit.setText(img1)
        self.lineEdit_3.setText(img2)


        ## 사진 보여주는 코드 ###
        # 첫번 째 사진
        self.pushButton_2.setStyleSheet(f"border-image:url(\'Man_hair/{fname[c_cup[round][j]]}\');",)
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(f"border-image:url(\'Man_hair/{fname[c_cup[round][j+1]]}\');")


        # 버튼에 커서 올릴 시 커서 활성화
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                    ### 사용자에게 입력받기 ###

        self.pushButton_2.clicked.connect(self.selected1)
        self.pushButton_3.clicked.connect(self.selected2)

    #첫번째 이미지를 택한 경우
    def selected1(self):
        global j,round
        c_cup[int(round / 2)].append(c_cup[round][j])  # 현재 round에서 선택한 결과를 다음 round의 리스트에 추가(append)한다.
        j += 2

        # 라운드가 끝나면 새로운 라운드로 시작
        if j == round:
            round = int(round / 2)
            j = 0

        if round == 1 :
            self.final1()

        print(c_cup)
        self.lineEdit_2.setText(f'{round}강 {int((j + 2) / 2)}/{int(round / 2)}')
        self.lineEdit.setText(get_name(fname[c_cup[round][j]]))
        self.lineEdit_3.setText(get_name(fname[c_cup[round][j + 1]]))

        ## 사진 보여주는 코드 ###
        # 첫번 째 사진
        self.pushButton_2.setStyleSheet(
            f"border-image:url(\'Man_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'Man_hair/{fname[c_cup[round][j + 1]]}\');")





    # 두번째 이미지를 택한 경우
    def selected2(self):
        global j,round
        c_cup[int(round / 2)].append(c_cup[round][j+1])  # 현재 round에서 선택한 결과를 다음 round의 리스트에 추가(append)한다.
        j+=2

        # 라운드가 끝나면 새로운 라운드로 시작
        if j == round :
            round = int(round / 2)
            j = 0

        if round == 1 :
            self.final1()

        print(c_cup)
        self.lineEdit_2.setText(f'{round}강 {int((j + 2) / 2)}/{int(round / 2)}')
        self.lineEdit.setText(get_name(fname[c_cup[round][j]]))
        self.lineEdit_3.setText(get_name(fname[c_cup[round][j + 1]]))

        ## 사진 보여주는 코드 ###
        # 첫번 째 사진
        self.pushButton_2.setStyleSheet(
            f"border-image:url(\'Man_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'Man_hair/{fname[c_cup[round][j + 1]]}\');")


    def final1(self):

        global winner, winner_p
        winner = get_name(fname[c_cup[round][0]])   # 이름
        winner_p =fname[c_cup[round][0]]

        self.hide()  # 메인윈도우 숨김
        self.final01 = NewWindw_final()
        self.final01.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()



###############################################여성 헤어 월드컵 #######################################

class NewWindw_02(QDialog,QWidget,form_hair1):
    def __init__(self):
        super(NewWindw_02, self).__init__()
        self.initUi()
        self.show()

        self.graphicsView_2.setStyleSheet(f"border-image:url(\'MaplePicture/pokemon.png\');")

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)
        # 콤보박스에서 목록 선택 시 이벤트 발생
        self.comboBox.currentIndexChanged.connect(self.printShtname)
        # 월드컵 실행창 활성화
        self.pushButton_2.clicked.connect(self.worldcup)

        #버튼에 커서 올릴 시 활성화
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.



    def worldcup(self):
        self.hide()  # 메인윈도우 숨김
        self.thrd = NewWindw2()
        self.thrd.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.

    # 콤보박스의 내용 변경시 터미널에 시트명 출력
    def printShtname(self):
        global play
        play = self.comboBox.currentText()




class NewWindw2(QDialog,QWidget,form_thrdwindow):
    def __init__(self):
        super(NewWindw2, self).__init__()
        self.initUi()
        self.show()


        self.graphicsView.setStyleSheet(f"border-image:url(\'MaplePicture/pokemon.png\');")
        self.graphicsView_2.setStyleSheet(f"border-image:url(\'MaplePicture/map2.jpg\');")

        # 월드컵 시작
        self.WorldCup()
        global round
        round = rounds
        self.select_items()

        # 이벤트 함수 조건
        self.pushButton_2.clicked.connect(self.btn_second_to_main)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.

    def WorldCup(self):
        global c1, c2, filenamelist, c4, c8, c16, c32, c0, c_cup, fname
        filenamelist = os.listdir('Girl_hair')
        c1 = []  # 승자
        c2 = []  # 2강
        c4 = []  # 4강
        c8 = []  # 8강
        c16 = []  # 16강
        c32 = []  # 32강
        c0 = []  # 처음에 사용자가 입력한 round에 따른 초기화 값을 저정함.
        c_cup = {1: c1, 2: c2, 4: c4, 8: c8, 16: c16, 32: c32}
        fname = []  # 파일이름

        for filenames in filenamelist:
            fname.append(filenames)
            random.shuffle(fname)

        # 라운드 셋팅
        global rounds

        # 선택값으로 초기화하기
        rounds = int(play[:-1])  # 2,4,8,16 ...
        for i in range(rounds):
            c0.append(i)
        c_cup[rounds] = c0  # 초기화한 값

        # 게임을 수행하는 부분.

    def select_items(self):  # round로 올 수 있는 값 : 64/32/16/8/4/2
        global get_name
        get_name = lambda x: x.split('.')[0]  # 파일명만 가져오도록 하는 간단한 함수.
        global j
        print(c_cup)

        j = 0
        self.select_items2(round)

    def select_items2(self, round):

        global img1, img2, j

        self.lineEdit_2.setText(f'{round}강 {int((j + 2) / 2)}/{int(round / 2)}')
        img1 = get_name(fname[c_cup[round][j]])
        img2 = get_name(fname[c_cup[round][j + 1]])
        self.lineEdit.setText(img1)
        self.lineEdit_3.setText(img2)

        ## 사진 보여주는 코드 ###
        # 첫번 째 사진
        self.pushButton_4.setStyleSheet(
            f"border-image:url(\'Girl_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'Girl_hair/{fname[c_cup[round][j + 1]]}\');")

        # 푸쉬버튼 위에 마우스 올릴 때 커서 활성화
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ### 사용자에게 입력받기 ###

        self.pushButton_4.clicked.connect(self.selected1)
        self.pushButton_3.clicked.connect(self.selected2)

    # 첫번째 이미지를 택한 경우
    def selected1(self):
        global j, round
        c_cup[int(round / 2)].append(c_cup[round][j])  # 현재 round에서 선택한 결과를 다음 round의 리스트에 추가(append)한다.
        j += 2

        # 라운드가 끝나면 새로운 라운드로 시작
        if j == round:
            round = int(round / 2)
            j = 0

        if round == 1 :
            self.final1()

        print(c_cup)
        self.lineEdit_2.setText(f'{round}강 {int((j + 2) / 2)}/{int(round / 2)}')
        self.lineEdit.setText(get_name(fname[c_cup[round][j]]))
        self.lineEdit_3.setText(get_name(fname[c_cup[round][j + 1]]))

        ## 사진 보여주는 코드 ###
        # 첫번 째 사진
        self.pushButton_4.setStyleSheet(
            f"border-image:url(\'Girl_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'Girl_hair/{fname[c_cup[round][j + 1]]}\');")




    # 두번째 이미지를 택한 경우
    def selected2(self):
        global j, round
        c_cup[int(round / 2)].append(c_cup[round][j + 1])  # 현재 round에서 선택한 결과를 다음 round의 리스트에 추가(append)한다.
        j += 2

        # 라운드가 끝나면 새로운 라운드로 시작
        if j == round:
            round = int(round / 2)
            j = 0

        if round == 1 :
            self.final1()

        print(c_cup)
        self.lineEdit_2.setText(f'{round}강 {int((j + 2) / 2)}/{int(round / 2)}')
        self.lineEdit.setText(get_name(fname[c_cup[round][j]]))
        self.lineEdit_3.setText(get_name(fname[c_cup[round][j + 1]]))

        ## 사진 보여주는 코드 ###
        # 첫번 째 사진
        self.pushButton_4.setStyleSheet(
            f"border-image:url(\'Girl_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'Girl_hair/{fname[c_cup[round][j + 1]]}\');")


    def final1(self):

        global winner, winner_p
        winner = get_name(fname[c_cup[round][0]])   # 이름
        winner_p =fname[c_cup[round][0]]

        self.hide()  # 메인윈도우 숨김
        self.final02 = NewWindw_final1()
        self.final02.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()




##################################최종 우승자 페이지############################################

class NewWindw_final(QDialog,QWidget,form_final):
    def __init__(self):
        super(NewWindw_final, self).__init__()
        self.initUi()
        self.show()


        # 이벤트 함수 조건
        self.pushButton_2.clicked.connect(self.btn_second_to_main)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # #우승자 페이지 화면
        self.graphicsView.setStyleSheet(f"border-image:url(\'Man_hair/{winner_p}\');")
        self.lineEdit.setText(winner)

    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.hide()  # 메인윈도우 숨김
        self.last1 = last_page()
        self.last1.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.





class NewWindw_final1(QDialog,QWidget,form_final):
    def __init__(self):
        super(NewWindw_final1, self).__init__()
        self.initUi()
        self.show()

        # 이벤트 함수 조건
        self.pushButton_2.clicked.connect(self.btn_return)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # #우승자 페이지 화면
        self.graphicsView.setStyleSheet(f"border-image:url(\'Girl_hair/{winner_p}\');")
        self.lineEdit.setText(winner)

    def initUi(self):
        self.setupUi(self)

    def btn_return(self):
        self.hide()  # 메인윈도우 숨김
        self.last11 = last_page()
        self.last11.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.



#######################이상형 월드컵 결과를 가져온 페이지#############################

class last_page(QDialog,QWidget,form_last):
    def __init__(self):
        super(last_page, self).__init__()
        self.initUi()
        self.show()

        self.label_2.setStyleSheet(f"border-image:url(\'MaplePicture/i15523914217.jpg\');")

        self.lineEdit.setText(winner)
        # self.Label_1 = QLabel(self)
        global input_p

        if name !=0 :
            self.lineEdit_2.setText(name)
            self.graphicsView_2.setStyleSheet(f"border-image:url(\'{input_p}\');")

        if fname1 !=0 :
            self.graphicsView.setStyleSheet(f"border-image:url(\'{input_p}\');")



        # 변수명 변경
        self.pushButton_3.clicked.connect(self.filedialog_open)

        # 최종 코디 추천 프로그램 실행
        self.pushButton_4.clicked.connect(self.output1)
        self.pushButton_5.clicked.connect(self.names1)
        self.lineEdit_2.returnPressed.connect(self.names1)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


    def initUi(self):
        self.setupUi(self)

    def filedialog_open(self):
        fnames = QFileDialog.getOpenFileName(self)
        global input_p
        input_p = fnames[0]

        self.graphicsView.setStyleSheet(f"border-image:url(\'{input_p}\');")


    def names1(self):
        global name
        # 파일이 있는경우 삭제 하는 함수
        file_path = f"{3}.jpg"

        if os.path.exists(file_path):
            os.remove(file_path)

        # 메이플 지지에서 캐릭터 정보를 가져오는 함수.
        Nickname = []
        name = self.lineEdit_2.text()
        url = f'https://maple.gg/u/{name}'
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            img = soup.find_all("div", class_="col-6 col-md-8 col-lg-6")
            for i in img:
                Nickname.append(i.find('img')['src'])
            img = Nickname[0]
            dload.save(img, f'{3}.jpg')
            self.graphicsView_2.setStyleSheet(f"border-image:url(\'3.jpg\');")

        else:
            print(response.status_code)
            print("NOT FOUND ONE MORE TIME")

        global input_p
        input_p = '3.jpg'


    def output1(self):
        global choice
        # 재 실행시 원래 있는 jpg 삭제하는 함수
        import os
        for i in range(3):
            file_path = f"{i}.jpg"

            if os.path.exists(file_path):
                os.remove(file_path)

        #색상 추출 할 사진
        photo = input_p

        # 모델 먼저 불러오기  모델 > 랜덤 포레스트
        cody_data = pd.read_csv('./cody_data.csv', encoding='euc-kr', index_col=0)

        # X, y 분리
        X = cody_data.drop('target', axis=1)
        y = cody_data['target']

        # 랜덤 포레스트 모델 생성 및 예측
        rf = RandomForestClassifier(n_jobs=-1)
        rf.fit(X, y)

        img_array = np.fromfile(photo, np.uint8)
        images = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

        # RGB 평균 구하기
        arr1 = images[:, :, 0].reshape(-1)
        r_mean = arr1[arr1 != 0].mean()

        arr1 = images[:, :, 1].reshape(-1)
        g_mean = arr1[arr1 != 0].mean()

        arr1 = images[:, :, 2].reshape(-1)
        b_mean = arr1[arr1 != 0].mean()

        # RGB 사이의 차이값 구하기
        rb_diff = abs(r_mean - b_mean)
        rg_diff = abs(r_mean - g_mean)
        gb_diff = abs(g_mean - b_mean)

        pix = cv2.cvtColor(images, cv2.COLOR_BGR2HSV)
        pix_h_data = pix[:, :, 0].reshape(-1)  # H부분만 추출
        # all_mean_v = pix[:,:,2].reshape(-1).mean()  #전체 평균 v

        unique, counts = np.unique(pix_h_data, return_counts=True)
        color_dict = dict(zip(unique, counts))
        sort_color = dict(sorted(color_dict.items(), key=lambda x: x[1], reverse=True)).keys()
        color_data = pd.DataFrame({'h_mean': [(np.array(list(sort_color))[0:6]).mean()]})  # 대표색상 6개의 평균

        color_data['r_mean'] = r_mean
        color_data['g_mean'] = g_mean
        color_data['b_mean'] = b_mean

        color_data['rb_diff'] = rb_diff
        color_data['rg_diff'] = rg_diff
        color_data['gb_diff'] = gb_diff

        # 모델을 통한 색상 예측
        print(rf.predict(color_data))

        global color_pred
        color_pred = rf.predict(color_data)[0]

        item_list = ['Cash', 'Hat', 'Overall']
        final_data = pd.read_csv('final_data2.csv', encoding='euc-kr', index_col=0)
        choice = []

        # 랜덤으로 3개를 추출하여 id를 리스트에 저장
        for item_category in item_list:
            choice.append(final_data[(final_data['color_pred'] == color_pred) &
                                     (final_data['item_category'] == item_category)]['item_id'].sample(3).tolist())

        ## 헤어 월드컵 우승 item_id 출력하는 함수
        Black_Hair = pd.read_csv('BlackHair.csv', encoding='utf-8')
        Hair1 = Black_Hair[Black_Hair['item_name'] == winner]
        print(Black_Hair['item_id'])
        Hair1.reset_index(drop=True, inplace=True)
        Hair1.reset_index(drop=True, inplace=True)
        Hair_id = Hair1['item_id'][0]


        # 코디 리스트가 들어갈 곳
        url_list = []

        # API 호출 및 코디 이미지 불러오기
        for i in range(3):
            hair_code = {"itemId": Hair_id, "version": "367", "region": "KMS"}
            cash_code = {"itemId": choice[0][i], "version": "367", "region": "KMS"}
            hat_code = {"itemId": choice[1][i], "version": "367", "region": "KMS"}
            overall_code = {"itemId": choice[2][i], "version": "367", "region": "KMS"}
            face_code = {"itemId": face, "version": "367", "region": "KMS"}
            skin_code1 = {"itemId": 2016, "version": "367", "region": "KMS"}
            skin_code2 = {"itemId": 12016, "version": "367", "region": "KMS"}

            url = f'https://maplestory.io/api/character/{skin_code1},{skin_code2},{hair_code},{cash_code},{hat_code},{overall_code},{face_code}/stand1/0?showears=false&showLefEars=false&showHighLefEars=undefined&resize=1&name=&flipX=false&bgColor=0,0,0,0'
            response = requests.get(url)

            image_url = response.url
            print(f'-------{i}번째 코디------')
            print(image_url, '\n')
            url_list.append(image_url)


        for i in range(len(url_list)):
            img = url_list[i]
            dload.save(img, f'{i}.jpg')

        # 아이템 이름 추출
        global item_name
        a = final_data[final_data['item_id'] == choice[0][0]]['item_name']
        a = []
        for j in range(3):
            for i in range(3):
                a.append(final_data[final_data['item_id'] == choice[j][i]]['item_name'])
        for i in range(len(a)):
            a[i].reset_index(drop=True, inplace=True)
        item_name = []
        for i in range(len(a)):
            item_name.append(a[i][0])


        # 머신러닝이 끝나면 파일을 실행하기
        self.hide()  # 메인윈도우 숨김
        self.output2 = output()
        self.output2.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.







#############################마지막 색깔별 코디 추천 페이지#########################


class output(QDialog,QWidget,form_output):
    def __init__(self):
        global input_p
        super(output, self).__init__()
        self.initUi()
        self.show()

        # bgm
        pygame.mixer.init()
        pygame.mixer.music.load('메이플스토리 BGM - 시그너스의 정원.mp3')
        pygame.mixer.music.play()

        self.graphicsView_4.setStyleSheet(f"border-image:url(\'MaplePicture/map4.jpg\');")
        self.graphicsView.setStyleSheet(f"border-image:url(\'0.jpg\');")
        self.graphicsView_2.setStyleSheet(f"border-image:url(\'1.jpg\');")
        self.graphicsView_3.setStyleSheet(f"border-image:url(\'2.jpg\');")

        self.lineEdit_2.setText(winner)
        self.lineEdit_3.setText(item_name[3])
        self.lineEdit_4.setText(item_name[6])
        self.lineEdit_5.setText(item_name[0])
        self.lineEdit_6.setText(winner)
        self.lineEdit_7.setText(item_name[4])
        self.lineEdit_8.setText(item_name[7])
        self.lineEdit_9.setText(item_name[1])
        self.lineEdit_10.setText(winner)
        self.lineEdit_11.setText(item_name[5])
        self.lineEdit_12.setText(item_name[8])
        self.lineEdit_13.setText(item_name[2])

        self.lineEdit.setText(f'{color_pred} 색상 코디 추천 목록')

        self.pushButton.clicked.connect(self.end)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # 콤보박스에서 목록 선택 시 이벤트 발생
        self.comboBox.currentIndexChanged.connect(self.printShtname2)
        self.comboBox_2.currentIndexChanged.connect(self.printShtname3)
        self.comboBox_3.currentIndexChanged.connect(self.printShtname4)


    def initUi(self):
        self.setupUi(self)

    # 콤보박스의 내용 변경시 터미널에 시트명 출력
    def printShtname2(self):
        global good1
        good1 = self.comboBox.currentText()

    def printShtname3(self):
        global good2
        good2 = self.comboBox_2.currentText()

    def printShtname4(self):
        global good3
        good3 = self.comboBox_3.currentText()

    def end(self):
        all_id = []
        for i in range(3):
            for j in range(3):
                all_id.append(choice[i][j])
        query = "INSERT INTO maple (item_id, score) VALUES (%s, %s)"

        with con:
            with con.cursor() as cur:
                cur.execute(query, (all_id[0], good1))
                cur.execute(query, (all_id[3], good1))
                cur.execute(query, (all_id[6], good1))
                cur.execute(query, (all_id[1], good2))
                cur.execute(query, (all_id[4], good2))
                cur.execute(query, (all_id[7], good2))
                cur.execute(query, (all_id[2], good3))
                cur.execute(query, (all_id[5], good3))
                cur.execute(query, (all_id[8], good3))
                con.commit()
                print("완료")
        print(good1,good2,good3)
        # csv파일로 사용자가 입력하는 결과물의 선호도 데이터를 저장하여 선호도 기반으로 강화학습.


        self.close()

############################ 실행함수 ########################################
if __name__ == "__main__":
    app =QApplication(sys.argv)
    main_dialog = auto_w() #해당부분 위 class name과 동일하게 작성
    main_dialog.show()
    QApplication.processEvents()
    app.exit(app.exec_())
    app.exec_()

