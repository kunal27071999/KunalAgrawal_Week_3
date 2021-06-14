"""
11. Create student class with instance variables as name and marks. Create student objects and use magic methods to compare the marks of students. Print the topper between three students.

"""

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __lt__(self, mar1):
        m1=self.marks
        m2=mar1.marks
        if(m1>m2):
            return self.name
        elif(m2>m1 ):
            return mar1.name

ob1=student('a',40)
ob2=student('b',30)
ob3=student('c',20)
print(ob2>ob1, " highest marks")
print(ob2>ob3,"  second highest marks")
