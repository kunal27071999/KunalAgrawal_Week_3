"""
13. WAP program using Que 8. 
   - At the end of the program print "Program completed successfully" using finally block
"""
try:
    a=int(input())
    b=int(input())
    print(a//b)
except ValueError as e:
    print("Value not provided")

except:
    print("Division by zero")

finally:
    print("Program completed successfully")