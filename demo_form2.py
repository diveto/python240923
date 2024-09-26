# demo_form.py는 Business Logic
# demo_form.ui는 Design Form

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import requests
from bs4 import BeautifulSoup

# 디자인파일 로딩
form_class = uic.loadUiType('demo_form2.ui')[0]

# 폼클래스 정의
class DemoForm(QMainWindow, form_class):
    # 초기화
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    # 슬롯 메소드
    def firstClick(self):
        url = 'https://www.daangn.com/fleamarket/'
        response = requests.get(url)

        # 검색이 용이한 Soup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')

        # 상단의 <div> 태그 찾기
        # div = soup.find('div', class_='card-desc')

        # 상단의 <div> 태그를 검색하고 파일로 저장
        f = open('daangn.txt', 'wt', encoding='utf-8')
        posts = soup.find_all('div', attrs={'class':'card-desc'})

        for post in posts:
            titleElement = post.find('h2', attrs={'class':'card-title'})
            priceElement = post.find('div', attrs={'class':'card-price'})
            regionElement = post.find('div', attrs={'class':'card-region-name'})

            title = titleElement.text.strip()
            price = priceElement.text.strip()
            region = regionElement.text.strip()

            # f-string 사용
            print(f'제목: {title}, 가격: {price}, 지역: {region}')
            f.write(f'제목: {title}, 가격: {price}, 지역: {region}\n')

        f.close()

        self.label.setText('당근마켓 크롤링 완료')

    def secondClick(self):
        self.label.setText('두번째버튼 클릭')

    def thirdClick(self):
        self.label.setText('세번째버튼 클릭')        

# 진입점 체크
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()