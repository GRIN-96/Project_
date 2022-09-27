
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
form_class = uic.loadUiType("test.ui")[0]
#################sec.ui 가져오기########################
form_secondwindow = uic.loadUiType("sec.ui")[0]
#################thrd.ui 가져오기########################
form_thrdwindow = uic.loadUiType("thrd.ui")[0]
###############man_hair.ui 가져오기#####################
form_hair = uic.loadUiType("man_hair.ui")[0]
###############girl_hair.ui 가져오기#####################
form_hair1 = uic.loadUiType("girl_hair.ui")[0]
###############final_page.ui 가져오기#####################
form_final = uic.loadUiType("final_page.ui")[0]
################last_page.ui 가져오기#####################
form_last = uic.loadUiType("last_page.ui")[0]
##################output.ui 가져오기#####################
form_output = uic.loadUiType("output.ui")[0]
#######################################################


class auto_w(QMainWindow,form_class): #class name 변경
    def __init__(self):
        global input_p
        input_p = 0
        super().__init__()
        self.setupUi(self)

        self.label_2.setStyleSheet(f"border-image:url(\'./i15523914217.jpg\');")


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
        global input_p
        fname1 = QFileDialog.getOpenFileName(self)
        input_p = fname1[0]
        self.graphicsView.setStyleSheet(f"border-image:url(\'{input_p}\');")

###############################################남성 헤어 월드컵 #######################################

class NewWindw_01(QDialog,QWidget,form_hair):
    def __init__(self):
        super(NewWindw_01, self).__init__()
        self.setupUi(self)
        self.show()

        self.graphicsView_2.setStyleSheet(f"border-image:url(\'./pokemon.png\');")

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

        self.graphicsView.setStyleSheet(f"border-image:url(\'./pokemon.png\');")
        self.graphicsView_2.setStyleSheet(f"border-image:url(\'./map1.jpg\');")

        # 월드컵 시작
        self.WorldCup()
        global round
        round = rounds
        self.select_items()

        # 이벤트 함수 조건
        self.pushButton.clicked.connect(self.btn_second_to_main)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.
        # print(play)
        # print(fname)
        # print(c0)

    def WorldCup(self):
        global c1, c2, filenamelist, c4, c8, c16, c32, c0, c_cup, fname
        filenamelist = os.listdir('./Man_hair')
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
        rounds = int(play[:-1]) # 2,4,8,16 ...
        for i in range(rounds):
            c0.append(i)
        c_cup[rounds] = c0  # 초기화한 값



        # 게임을 수행하는 부분.
    def select_items(self):  # round로 올 수 있는 값 : 64/32/16/8/4/2
        global get_name
        # random.shuffle(c_cup[round])  # 현재 round 시작 전에 리스트의 값을 랜덤하게 섞어준다.
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
        self.pushButton_2.setStyleSheet(f"border-image:url(\'./Man_hair/{fname[c_cup[round][j]]}\');",)
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(f"border-image:url(\'./Man_hair/{fname[c_cup[round][j+1]]}\');")

                    ### 사용자에게 입력받기 ###

        self.pushButton_2.clicked.connect(self.selected1)
        self.pushButton_3.clicked.connect(self.selected2)



            # global winner,winner_p
            # winner = get_name(fname[c_cup[round][j+1]])   # 이름
            # winner_p = f"border-image:url(\'C:/Users/playdata/Desktop/test/Man_hair/{fname[c_cup[round][j + 1]]}\');"
            # self.hide()  # 메인윈도우 숨김
            # self.f_page = NewWindw_final()
            # self.f_page.exec()  # 두번째 창을 닫을 때 까지 기다림
            # self.close()  # 클릭시 종료됨.


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
            f"border-image:url(\'./Man_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'./Man_hair/{fname[c_cup[round][j + 1]]}\');")





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
            f"border-image:url(\'./Man_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'./Man_hair/{fname[c_cup[round][j + 1]]}\');")


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

        self.graphicsView_2.setStyleSheet(f"border-image:url(\'./pokemon.png\');")

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

        self.graphicsView.setStyleSheet(f"border-image:url(\'./pokemon.png\');")
        self.graphicsView_2.setStyleSheet(f"border-image:url(\'./map2.jpg\');")

        # 월드컵 시작
        self.WorldCup()
        global round
        round = rounds
        self.select_items()

        # 이벤트 함수 조건
        self.pushButton_2.clicked.connect(self.btn_second_to_main)



    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        self.close()  # 클릭시 종료됨.

    def WorldCup(self):
        global c1, c2, filenamelist, c4, c8, c16, c32, c0, c_cup, fname
        filenamelist = os.listdir('./Girl_hair')
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
        # random.shuffle(c_cup[round])  # 현재 round 시작 전에 리스트의 값을 랜덤하게 섞어준다.
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
            f"border-image:url(\'./Girl_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'./Girl_hair/{fname[c_cup[round][j + 1]]}\');")

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
            f"border-image:url(\'./Girl_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'./Girl_hair/{fname[c_cup[round][j + 1]]}\');")


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
            f"border-image:url(\'./Girl_hair/{fname[c_cup[round][j]]}\');", )
        ### 두번 째 사진
        self.pushButton_3.setStyleSheet(
            f"border-image:url(\'./Girl_hair/{fname[c_cup[round][j + 1]]}\');")


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

        # #우승자 페이지 화면
        print(winner_p)
        print(winner)
        self.graphicsView.setStyleSheet(f"border-image:url(\'./Man_hair/{winner_p}\');")
        self.lineEdit.setText(winner)

    def initUi(self):
        self.setupUi(self)

    def btn_second_to_main(self):
        print("실행됨")
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

        # #우승자 페이지 화면
        print(winner_p)
        print(winner)
        self.graphicsView.setStyleSheet(f"border-image:url(\'./Girl_hair/{winner_p}\');")
        self.lineEdit.setText(winner)

    def initUi(self):
        self.setupUi(self)

    def btn_return(self):
        print("실행됨")
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

        self.label_2.setStyleSheet(f"border-image:url(\'./i15523914217.jpg\');")

        self.lineEdit.setText(winner)
        # self.Label_1 = QLabel(self)
        global input_p
        if input_p != 0:
            self.graphicsView.setStyleSheet(f"border-image:url(\'{input_p}\');")
            print("실행됨.")

        # 변수명 변경
        self.pushButton_3.clicked.connect(self.filedialog_open)

        # 최종 코디 추천 프로그램 실행
        self.pushButton_4.clicked.connect(self.output1)

    # 이벤트 함수 조건
        # self.pushButton_2.clicked.connect(self.btn_return)


    def initUi(self):
        self.setupUi(self)

    def filedialog_open(self):
        fnames = QFileDialog.getOpenFileName(self)
        # fnames = QFileDialog.getOpenFileName(self, "Open File", "", All files(*) Image File(*.png *.jpg))
        print(fnames)
        global input_p
        input_p = fnames[0]
        print(input_p)

        self.graphicsView.setStyleSheet(f"border-image:url(\'{input_p}\');")


    def output1(self):
        self.hide()  # 메인윈도우 숨김
        self.output2 = output()
        self.output2.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.close()  # 클릭시 종료됨.





#############################마지막 색깔별 코디 추천 페이지#########################


class output(QDialog,QWidget,form_output):
    def __init__(self):
        global color
        color = "GREEN"
        super(output, self).__init__()
        self.initUi()
        self.show()

        self.graphicsView_4.setStyleSheet(f"border-image:url(\'./커닝.jpg\');")

        self.lineEdit.setText(f'{color} 색상 코디 추천 목록')

        self.pushButton.clicked.connect(self.end)


    def initUi(self):
        self.setupUi(self)

    def end(self):
        self.close()





############################ 실행함수 ########################################
if __name__ == "__main__":
    app =QApplication(sys.argv)
    main_dialog = auto_w() #해당부분 위 class name과 동일하게 작성
    main_dialog.show()
    QApplication.processEvents()
    app.exit(app.exec_())
    app.exec_()

#
