# DemoListTuple.py

strA = '파이썬은 강력해'
strB = 'Python is very powerful'
x = 100
y = 3.14


print(dir())
print(len(strA))
print(len(strB))


strC = '''다중 라인을
저장하는 경우는
이렇게 처리한다.
'''

print(strC)


print(strA[0] * 3)
print(strA[0:3])
print(strA[:5])
print(strA[-3:])

print('\nTuple -----------------------------------------------------')

# 튜플
tp = (10, 20, 30)
print(len(tp))

# 함수정의
def calc(a, b):
    return a+b, a*b

# 함수호출
result = calc(3, 4)
print(result)

print('id: %s, name: %s' % ('kim', '김유신'))

print('\nType casting ---------------------------------------------')

a = set((10, 20, 30))
print(a)
print(type(a))

b = list(a)
print(b)
b.append(40)
print(b)
print(type(b))

c = tuple(b)
print(c)
print(type(c))