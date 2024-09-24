# DemoLoop.py

print('\nwhile ---------------')
value = 5
while value < 8:
    print(value)
    value += 1

print('\nfor in ---------------')
lst = [100, 3.14, 'demo']
for item in lst:
    print(item)

print('\nrange() ---------------')
years = list(range(2000, 2025))
print(years)
days = list(range(1, 32))
print(days)

print('\nlist comprehension. ---------------')
lst = list(range(1, 11))
print(lst)
print([i**2 for i in lst if i > 5])

d = {100:'apple', 200:'kiwi'}
print([v.upper() for v in d.values()])

tp = ('apple', 'kiwi')
print([len(i) for i in tp])

print('\nfiltering --------------------------------')
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print('\ncutom filtering --------------------------------')
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print('\nlambda ------------------------------------')
iterL = filter(lambda x:x>25, lst)
for item in iterL:
    print(item)