import sqlite3

# 파일에 저장
con = sqlite3.connect('c:\\work\\sample.db')
# SQL구문은 커서객체 실행
cur = con.cursor()
# 테이블 구조를 생성(테이블 스키마)
cur.execute('create table if not exists PhoneBook (Name text, PhoneNum text);')
# 1건을 입력 - ', " 구분해서 사용
cur.execute('insert into PhoneBook values ("김길동", "010-1111-1111");')

# 입력 파라메터 처리
# 입력 파라메터는 튜플로 전달
name = '전우치'
phoneNumber = '010-9999-9999'
cur.execute('insert into PhoneBook values (?, ?);', (name, phoneNumber))

# 다중의 행을 처리
datalist = (("이길동", "010-2222-2222"), ("최길동", "010-3333-3333"))

cur.executemany('insert into PhoneBook values (?, ?);', datalist)

# 검색 - 튜플로 반환
cur.execute('select * from PhoneBook;')
for row in cur:
    print(row[0], row[1])

# 완료 COMMIT
con.commit()