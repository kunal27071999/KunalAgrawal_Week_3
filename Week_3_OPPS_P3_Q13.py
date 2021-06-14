"""
13. Method Overriding: Create class Area and define display method using below 
	- Display method will take circle redious as parameter, calculate the area and prints it.
	- Display method will take rectangle lenght and width as parameter, calculate the area and prints it.
	- Display method will take Cube lenght, width and height as parameter, calculate the area and prints it.

"""
class area:
    def cal(self, x = None, y = None,z=None):
        if x != None and y != None:
            return x * y
        elif x != None and y != None and z!=None:
            return x * y
        else:
            return (3.14*x*x)

ob1=area()
print(ob1.cal(5,10))
