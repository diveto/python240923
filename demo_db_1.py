import sqlite3

# 메모리에 임시로 저장
con = sqlite3.connect(':memory:')
# SQL구문은 커서객체 실행
cur = con.cursor()
# 테이블 구조를 생성(테이블 스키마)
cur.execute('create table PhoneBook (Name text, PhoneNum text);')
# 1건을 입력 - ', " 구분해서 사용
cur.execute('insert into PhoneBook values ("김길동", "010-1111-1111");')
# 검색 - returns Tuple
cur.execute('select * from PhoneBook;')

for row in cur:
    print(row[0], row[1])