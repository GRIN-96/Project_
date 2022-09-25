
# -- coding: utf-8 --


import sys
from PyQt5.QtWidgets import *
import os
from PyQt5 import QtWidgets, uic
import random


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
###############man_hair.ui 가져오기#####################
form_hair = uic.loadUiType("man_hair.ui")[0]
###############girl_hair.ui 가져오기#####################
form_hair1 = uic.loadUiType("girl_hair.ui")[0]
###############final_page.ui 가져오기#####################
form_final = uic.loadUiType("final_page.ui")[0]
#######################################################


class auto_w(QMainWindow,form_class): #class name 변경
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        # startButton 클릭시 autoExcute 함수 수행
        self.pushButton.clicked.connect(self.man_hair)
        self.pushButton_2.clicked.connect(self.girl_hair)

        # button 클릭시 함수 수행
        self.pushButton_3.clicked.connect(self.fileopen)


        # #헤어 월드컵 우승 text 가져오기
        # self.label_5.setText(f_img)


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
        global filename
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')

###############################################남성 헤어 월드컵 #######################################

class NewWindw_01(QDialog,QWidget,form_hair):
    def __init__(self):
        super(NewWindw_01, self).__init__()
        self.setupUi(self)
        self.show()

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)
        # 콤보박스에서 목록 선택 시 이벤트 발생
        self.comboBox.currentIndexChanged.connect(self.printShtname)
        # 월드컵 실행창 활성화
        self.pushButton_2.clicked.connect(self.worldcup)

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
        # print(self.comboBox.currentText())



class NewWindw(QDialog,QWidget,form_secondwindow):
    def __init__(self):
        super(NewWindw, self).__init__()
        self.setupUi(self)
        self.show()


        # 월드컵 시작
        a = WorldCup()
        a.db_setting()
        a.__init__()

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.
        # print(play)


class WorldCup(NewWindw):
    # global c1, c2, filenamelist, c4, c8, c16, c32, c64, c0, c_cup, fname
    filenamelist = os.listdir('C:/Users/playdata/Desktop/test/Man_hair')
    c1 = -1  # 승자
    c2 = []  # 2강
    c4 = []  # 4강
    c8 = []  # 8강
    c16 = []  # 16강
    c32 = []  # 32강
    c64 = []  # 64강
    c0 = []  # 처음에 사용자가 입력한 round에 따른 초기화 값을 저정함.
    c_cup = {1: c1, 2: c2, 4: c4, 8: c8, 16: c16, 32: c32, 64: c64}
    fname = []  # 파일이름


    for filenames in filenamelist:
        fname.append(filenames)
        random.shuffle(fname)

    ### 그림 파일 이름을 받아와서 랜덤하게 섞이.
    def db_setting(self):
        for filenames in self.filenamelist:
            self.fname.append(filenames)
            random.shuffle(self.fname)


    def __init__(self,round):
        super().__init__()

        self.select_items(round)
        if round == 2:
            NewWindw.textEdit.setText('결승전 시작')
        else:
            random.shuffle(self.c_cup[round])  # 현재 round 시작 전에 리스트의 값을 랜덤하게 섞어준다.
        get_name = lambda x: x.split('.')[0]  # 파일명만 가져오도록 하는 간단한 함수.

        for i in range(0, round, 2):
            NewWindw.textEdit.setText(f'{round}강 {int((i + 2) / 2)}/{int(round / 2)}')
            global img1
            global img2
            img1 = get_name(self.fname[self.c_cup[round][i]])
            img2 = get_name(self.fname[self.c_cup[round][i + 1]])
            NewWindw.textEdit_3.setText(img1)
            NewWindw.textEdit_4.setText(img2)

            ### 사진 보여주는 코드 ###
            ### 첫번 째 사진
            NewWindw.pushButton_2.setStyleSheet(f"border-image:url(\'C:/Users/playdata/Desktop/test/data/{self.fname[self.c_cup[round][i]]}');")
            ### 두번 째 사진
            NewWindw.pushButton_3.setStyleSheet(f"border-image:url(\'C:/Users/playdata/Desktop/test/data/{self.fname[self.c_cup[round][i+1]]}');")

            ### 사용자에게 입력받기 ###
            NewWindw.pushButton_2.clicked.connect(self.selected1)
            NewWindw.pushButton_3.clicked.connect(self.selected2)

            if round == 2:  # 결승전일 때
                NewWindw.pushButton_2.clicked.connect(self.final1)
                NewWindw.pushButton_3.clicked.connect(self.final2)

        if round != 2:
            round = int(round / 2)
            self.select_items(round)



    # ### 게임을 수행하는 부분.
    # def select_items(self,round):  # round로 올 수 있는 값 : 64/32/16/8/4/2
    #     global get_name

        # if round == 2:
        #     self.textEdit.setText('결승전 시작')
        # else:
        #     random.shuffle(self.c_cup[round])  # 현재 round 시작 전에 리스트의 값을 랜덤하게 섞어준다.
        # get_name = lambda x: x.split('.')[0]  # 파일명만 가져오도록 하는 간단한 함수.
        #
        # for i in range(0, round, 2):
        #     NewWindw.textEdit.setText(f'{round}강 {int((i + 2) / 2)}/{int(round / 2)}')
        #     global img1
        #     global img2
        #     img1 = get_name(self.fname[self.c_cup[round][i]])
        #     img2 = get_name(self.fname[self.c_cup[round][i + 1]])
        #     NewWindw.textEdit_3.setText(img1)
        #     NewWindw.textEdit_4.setText(img2)
        #
        #     ### 사진 보여주는 코드 ###
        #     ### 첫번 째 사진
        #     NewWindw.pushButton_2.setStyleSheet(f"border-image:url(\'C:/Users/playdata/Desktop/test/data/{self.fname[self.c_cup[round][i]]}');")
        #     ### 두번 째 사진
        #     NewWindw.pushButton_3.setStyleSheet(f"border-image:url(\'C:/Users/playdata/Desktop/test/data/{self.fname[self.c_cup[round][i+1]]}');")
        #
        #     ### 사용자에게 입력받기 ###
        #     NewWindw.pushButton_2.clicked.connect(self.selected1)
        #     NewWindw.pushButton_3.clicked.connect(self.selected2)
        #
        #     if round == 2:  # 결승전일 때
        #         NewWindw.pushButton_2.clicked.connect(self.final1)
        #         NewWindw.pushButton_3.clicked.connect(self.final2)
        #
        # if round != 2:
        #     round = int(round / 2)
        #     self.select_items(round)


    #     # 첫번째 이미지를 택한 경우
    def selected1(self):
        self.c_cup[int(round / 2)].append(img1)  # 현재 round에서 선택한 결과를 다음 round의 리스트에 추가(append)한다.
    # 두번째 이미지를 택한 경우
    def selected2(self):
        self.c_cup[int(round / 2)].append(img2)  # 현재 round에서 선택한 결과를 다음 round의 리스트에 추가(append)한다.


    def round_setting(self):  # round수 선택 받고, 초기화하기
        global round

        self.db_setting()  # db 섞기
        # 선택값으로 초기화하기
        rounds = int(play[:-1]) # 2,4,8,16 ...
        for round in range(rounds):
            self.c0.append(round)
        self.c_cup[rounds] = self.c0  # 초기화한 값
        ## rounds 입력값에 따른 select_items 매서드 시작 ###
        self.select_items(rounds)



    def final1(self):
        self.c_cup[int(round / 2)].append(img1)
        self.hide()  # 메인윈도우 숨김
        self.final = NewWindw_final()
        self.final.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.


    def final2(self):
        self.c_cup[int(round / 2)].append(img2)
        self.hide()  # 메인윈도우 숨김
        self.final = NewWindw_final()
        self.final.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.



###############################################여성 헤어 월드컵 #######################################

class NewWindw_02(QDialog,QWidget,form_hair1):
    def __init__(self):
        super(NewWindw_02, self).__init__()
        self.initUi()
        self.show()

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)
        # 콤보박스에서 목록 선택 시 이벤트 발생
        self.comboBox.currentIndexChanged.connect(self.printShtname)
        # 월드컵 실행창 활성화
        self.pushButton_2.clicked.connect(self.worldcup)

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
        print(self.comboBox.currentText())



class NewWindw2(QDialog,QWidget,form_thrdwindow):
    def __init__(self):
        super(NewWindw2, self).__init__()
        self.initUi()
        self.show()

        # 이벤트 함수 조건
        self.pushButton_2.clicked.connect(self.btn_second_to_main)



    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.
        print(play)



##################################최종 우승자 페이지############################################

class NewWindw_final(QDialog,QWidget,form_final):
    def __init__(self):
        super(NewWindw_final, self).__init__()
        self.initUi()
        self.show()

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)

        # 우승자 페이지 화면
        self.graphicsView.setStyleSheet(f"border-image:url(\'C:/Users/playdata/Desktop/test/data/{self.fname[self.c_cup[int(round / 2)]]}');")
        # global final_img
        # final_img = get_name(self.fname[self.c_cup[int(round / 2)]])
        # self.textEdit_2.setText(f_img)

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

