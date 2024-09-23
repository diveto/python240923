# func1.py

print('\nCall setValue -----------------------------------------------------')

# Define function
def setValue(newValue):
    # local VAR.
    x = newValue
    print("지역변수:", x)

# Call Function
retValue = setValue(10)
print(retValue)

print('\nCall swap -----------------------------------------------------')

# Define Function 2
def swap(x, y):
    return y, x

# Call Function 2
print(swap(3, 4))

print('\nCall intersect -----------------------------------------------------')

# Define Function 3
def intersect(preList, postList):
    result = []

    for x in preList:
        if x in postList and x not in result:
            result.append(x)

    return result

# Call Function 3
print(intersect('HAM', 'SPAM'))

# Define Function 4
print('\tCall times -----------------------------------------------------')

# 기본값을 명시
def times(a=10, b=20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(5, 6))

# 지역변수와 전역변수
x = 5
def func1(a):
    return a + x

print('Global', func1(1))

def func2(a):
    x = 3
    return a + x

print('Local', func2(1))