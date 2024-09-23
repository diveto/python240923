# func2.py

# 일반함수
def times(a, b):
    return a * b

# 람다함수정의

g = lambda x,y:x*y
print(g(3, 4))
print(g(4, 5))

print((lambda x:x*x)(3))

print(globals())