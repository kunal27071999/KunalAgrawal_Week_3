"""
15. WAP program using Que 10. 
   - At the end of the program print "Program completed successfully" using finally block
"""
try:
    a=int(input())
    b=int(input())
    print(a//b)

except (ArithmeticError, ZeroDivisionError, ValueError):
    print("Error occured")

finally:
    print("Program completed successfully")