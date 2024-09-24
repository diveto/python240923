# 파일 쓰기
f = open('demo.txt', 'wt', encoding='utf-8')
f.write('''첫번째
        두번째
        세번째

import 모듈

from 모듈 import 어트리뷰트
from 모듈 import *

form 패키지 import 모듈
from 패키지 import *
        ''')
f.close()

# 파일 읽기
f = open('demo.txt', 'rt', encoding='utf-8')
result = f.read()
f.close()
print(result)