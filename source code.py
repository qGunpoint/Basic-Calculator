print("--CALCULATOR--")
print()

# Using time import to prevent the .exe from closing out early.
import time

# Asks for user input. 
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
op = input("Enter a valid operator (+,-,*,/): ")

# If statements make the calculator actually function.
if op == "+":
    print(num1 + num2)
    time.sleep(100000000000000000000000000000000000000000000)
elif op == "-":
    print(num1 - num2)
    time.sleep(100000000000000000000000000000000000000000000)
elif op == "*":
    print(num1 * num2)
    time.sleep(100000000000000000000000000000000000000000000)
elif op == "/":
    print(num1 / num2)
    time.sleep(100000000000000000000000000000000000000000000)
else:
    print("Invalid operator.")
    time.sleep(100000000000000000000000000000000000000000000)
