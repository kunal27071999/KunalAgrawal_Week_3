"""
11. Try with default except block: WAP which will take two integer numbers as input and perform division of them.
	- User of this program is not smart and can input anything as part of input
	- Handle ZeroDivisionError and rest all should be catched in default block
	- Print exception information

"""

try:
    a=int(input())
    b=int(input())
    print(a//b)

except (ZeroDivisionError):
    print("ZeroDivisionError")

except(ArithmeticError, ValueError):
    print("ERROR occured")

