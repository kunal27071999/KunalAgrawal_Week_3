"""
12. Create an employee class with instance variables as name and "per days salary". Create class timesheet with name and days. use magic method to calculate the employees salary of the month.

"""
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class time(employee):
    def __init__(self,days):
        self.days=days
    def __rmul__(self, other):
        return (self.days*other.salary)

ob1=employee('a',10)
ob2=time(20)
print(ob1.name ," salary ",ob1 * ob2)
