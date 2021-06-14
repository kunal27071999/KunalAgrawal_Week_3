"""
25. Write note on interface in python.

"""
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def NumSide(self):
        pass
class Circle(Shape):
    def NumSide(self):
        print("Infinite sides")
class Rectangle(Shape):
    def NumSide(self):
        print("4 sides")
class Cube(Shape):
    def NumSide(self):
        print("12 sides")
s1=Cube()
s1.NumSide()
s2=Rectangle()
s2.NumSide()