x = input("Enter num 1:")
y = input("Enter num 2:")
try:
    z = x / int(y)
except ZeroDivisionError:
    print("Division by zero")
    z = None
except TypeError as e:
    print("Exception type: ", type(e).__name__)
    z = None
print("Division is: ", z)