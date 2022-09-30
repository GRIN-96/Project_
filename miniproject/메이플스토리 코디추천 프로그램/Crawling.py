# 셀레니움을 사용하기 위해 함수호출
import time
import urllib.request
import os
import requests
import re
import dload
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# driver = "C:/Users/user/Downloads/01_selenium/chromedriver.exe"

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://maple-r.github.io/")
time.sleep(3)

# 코디 시뮬레이터에서 카테고리 리스트 보기위해 클릭
driver.find_element(By.XPATH, r'//*[@id="opTog"]/i').click()
time.sleep(3)
# 얼굴, 헤어, 한벌옷등 카테고리 칸 클릭 ( 카테고리 Xpath 복사 )
driver.find_element(By.XPATH, r'//*[@id="Cashbtn"]').click()
time.sleep(3)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
images = soup.find_all("div", id="cashList")

# src 리스트 만들기
face_image = []
for one in images[0]:
    img_ = one.find('img')
    face_image.append(img_['src'])

print(face_image)

# title 리스트 만들기
name_list = []
nameList = soup.findAll(id="cashList")
for i in nameList[0]:
    name_list.append(i['title'])

print(name_list)
print(len(name_list))

# 이미지 저장
for i in range(len(face_image)):
    img = face_image[i]
    dload.save(img, f'{name_list[i]}.jpg')



# 카테고리 칸에서 항목별 XPATH 값만 변경해서 입력해주고
#
# id 값만 변경해주면 항목별로 이미지 다운로드가 가능한 코드 입니다.
#
# 저는 src 주소 리스트와  title 리스트를 따로 만들어
#
# 반복문으로 title을 이름으로 src를 가져와 jpg 형태로 저장했습니다.



########################메이플gg 에서 닉네임별 캐릭터 정보를 가져온 코드 ###########################


a = []
for num in range(1,201):
    url = f'https://maple.gg/rank/reboot?page={num}'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find_all("div", class_="d-inline-block mr-2 align-middle")

        for i in img:
            a.append(i.find('img')['src'])

    else :
        print(response.status_code)



for number, b in enumerate(a):
    urllib.request.urlretrieve(b, "C:/Users/tjdwp/Desktop/Crawling/Present/" + '{}.jpg'.format(number))
    print("저장중입니다.")

# list = pd.DataFrame(a)
# list.to_csv("C:/Users/tjdwp/Desktop/Crawling/MapleTwo.csv", mode='w')