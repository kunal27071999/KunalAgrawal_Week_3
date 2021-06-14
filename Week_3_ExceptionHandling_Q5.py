"""
5. WAP which takes two arguments as input. Perform division of two numbers. Handle the error/exception if divider is 0.
"""


try:
    a = int(input("Enter 1st number :"))
    b = int (input("Enter 2nd number :"))
    print(a//b)
except:
    print("Cannot divide with zero")