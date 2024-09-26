import requests
from bs4 import BeautifulSoup

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
     
# <div class="card-desc">
#       <h2 class="card-title">아이폰 14 128GB</h2>
#       <div class="card-price ">
#         600,000원
#       </div>
#       <div class="card-region-name">
#         전남 순천시 용당동
#       </div>