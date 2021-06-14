"""
10. Try with single except: WAP which will take two integer numbers as input and perform division of them.
	- User of this program is not smart and can input anything as part of input
	- Handle ArithmaticError, ZeroDivisionError and ValueError
	- Print exception information

"""
try:
    a=int(input())
    b=int(input())
    print(a//b)

except (ArithmeticError, ZeroDivisionError, ValueError):
    print("Error occured")
