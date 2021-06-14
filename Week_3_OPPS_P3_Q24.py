"""
24. Create class Shape by extending the ABC and declare abstract method displayNumOfSides. 
	- Create class Circle by extending Shape and try to initialize it.
	- Create class Circle, Rectangle and Cube by extending Shape. Provide implementation to method displayNumOfSides
	
    """

from abc import ABC, abstractmethod

class Student:
    @abstractmethod
    def display(self):
        pass
class ABC(Student):
    def display(self,n):
        print("Name of student is",n)

s1=ABC()
s1.display('b')

s2=ABC()
s2.display('a')