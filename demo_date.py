from datetime import *

d1 = date(2024, 9, 25)
print(d1)

d2 = date.today()
print(d2)

d3 = datetime.now()
print(d3)

d4 = timedelta(days = 100)
print('주문받고 100일 후', d2 + d4)

print('\n---------------------------------------')

# 임의의 숫자를 생성
import random

print(random.random())
print(random.random())
print(random.uniform(2.0, 5.0))
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

# 로또번호
# print(random.sample(range(1, 46), 6))

print('\n---------------------------------------')

# 파일명 다루기
from os.path import *
from os import *

# 절대경로
print(abspath('python.exe'))
# 상대경로
print(basename('c:\\work\\python.exe'))

fname = 'c:\\python310\\python.exe'
if exists(fname):
    print('파일크기', getsize(fname))
else:
    print('파일 없음')

print('운영체제명:', name)
print('환경변수목록:', environ)

# 외부 실행파일
# system('notepad.exe')

print('\n---------------------------------------')

# 파일목록
import glob
print(glob.glob('c:\\work\\*.py'))