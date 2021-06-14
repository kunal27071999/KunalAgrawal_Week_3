"""
9. Solve problem of Que 8 using magic method

"""
class Book:
    def __init__(self,a):
        self.a=a
    def __add__(self, o):
        return self.a+o

obj1=Book(100)
print(obj1+200)
