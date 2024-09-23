# func1.py

# Define function
def setValue(newValue):
    # local VAR.
    x = newValue
    print("지역변수:", x)

# Call Function
retValue = setValue(10)
print(retValue)

# Define Function 2
def swap(x, y):
    return y, x

# Call Function 2
print(swap(3, 4))