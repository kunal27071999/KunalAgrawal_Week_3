"""
16. WAP program using Que 11. 
   - At the end of the program print "Program completed successfully" using finally block
"""
try:
    a=int(input())
    b=int(input())
    print(a//b)

except (ZeroDivisionError):
    print("Division by zero")

except(ArithmeticError, ValueError):
    print("Exeception occured")

finally:
    print("Program completed successfully")
