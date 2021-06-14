"""
17. WAP to handle ArithmaticError in outer try except block and ZeroDivisionError in inner try except bolck. Use finally to print the "Program completed successfully"  message.

"""
try:
    a=int(input())
    b=int(input())
    try:
        print(a//b)
    except(ZeroDivisionError):
        print("Zero division error")
except(ArithmeticError):
    print("Arithmetic Error")
