"""
23. Create an abstract class as Student.
	- Initialize Student calss as : Student(). Mention the reasone of successful initialization of the Student calss. 
	- Extend class ABC and initialize Student calss as : Student(). Mention the reasone of successful initialization of the Student calss. 
	- Extend class ABC and Declare abstract method deplay() in the Student calss. try to initialize the class Student.
	- Declare abstract method deplay() in the Student calss. try to initialize the class Student.

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