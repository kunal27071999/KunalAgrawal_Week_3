"""
21. Create class "Shape" and Define method calculateArea which calculates the area of shape and declare an abstract method : display
	- Create class Circle which inherets the Shape class, implements the abstract display method. It calls calculateArea method to calculate the area of circle.
	- Create class Rectangle which inherets the Shape class, implements the abstract display method. It calls calculateArea method to calculate the area of circle.
	- Create class Cube which inherets the Shape class, implements the abstract display method. It calls calculateArea method to calculate the area of circle.

"""

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self,r):
        print("Area is",3.14*r*r)
class Rectangle(Shape):
    def area(self,l,b):
        print("Area is",l*b)

class Cube(Shape):
    def area(self,s):
        print("Area is",s*s)

s1=Circle()
s1.area(3)

s2=Rectangle()
s2.area(3,4)
