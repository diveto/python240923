# 크롤링 선언
from bs4 import BeautifulSoup

# html 파일 읽기
with open('Chap09_test.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 원하는 데이터 추출
# 1. 태그 추출
soup = BeautifulSoup(html, 'html.parser')

# 2. 태그 내용 추출
# print(soup.prettify())

# 3. 태그 내용 추출
# print(soup.find_all('p'))       

# 첫번쨰 <p> 태그 찾기
# print(soup.find('p'))

# 조건에 맞는 <p> 태그 찾기 
# print(soup.find_all('p', class_='outer-text'))

# 최근에는 attrs 속성 제공: 파이썬 내부에서 class 속성을 인식하지 못함 그래서 class_ 사용
# print(soup.find_all('p', attrs={'class':'outer-text'}))

# <p> 태그 내에서 id 속성 찾기
print(soup.find_all('p', attrs={'id':'first'}))

# 찾은 결과를 루프돌리기
for p in soup.find_all('p'):
    # 내부 컨텍스트만 출력
    title = p.text.strip()
    title = title.replace('\n', '')
    print(title)










