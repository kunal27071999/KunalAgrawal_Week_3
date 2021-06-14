"""
14. Solve above Que 13 using Default arguments

"""
from typing import overload
import math

class Area:

    @overload
    def area(l, b):
        return l * b

    @overload
    def area(r):
        return math.pi * r ** 2

    @overload
    def area(l,b,h):
        return l*b


a = Area()
a.area(10)
