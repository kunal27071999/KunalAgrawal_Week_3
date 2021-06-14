"""
29. Create class Student, declare the student name as pulic, student department as protected and studebt id as private.
	1. Define as method display which prints all the attribets of Student
	2. Create student class object object stud and try to print the attributesof the student outside the class using stud.attributename

"""
class Student:
    name=None
    _dept=None
    __id=None
    def __init__(self,name,dept,id):
        self.name=name
        self._dept=dept
        self.__id=id
    def display(self):
        print("Name :",self.name)
        print("Department :",self._dept)
        print("Id :",self.__id)

s1=Student('a','CSE',17)
s1.display()