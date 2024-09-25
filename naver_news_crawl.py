import requests
from bs4 import BeautifulSoup
import openpyxl

# URL 설정
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=반도체"

# 웹 페이지 요청
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get(url, headers=headers)

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 기사 제목과 URL 크롤링
titles = soup.find_all("a", class_="news_tit")

# 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "News Titles"
ws.append(["Index", "Title", "URL"])

# 데이터 엑셀에 저장
for idx, title in enumerate(titles, 1):
    news_title = title.get_text()
    news_url = title['href']
    ws.append([idx, news_title, news_url])

# 엑셀 파일 저장
wb.save("news_result.xlsx")
