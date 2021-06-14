"""
17. Using Que 16 details call parent class method using super method

"""
class shape:
    def areaCalculator( x = None, y = None,z=None):
        if x != None and y != None and z==None:
            return x * y
        elif x != None and y != None and z!=None:
            return x * y
        elif x!=None and y==None and z==None:
            return (3.14*x*x)
class Circle(shape):
    def disparea(a):
        print("Area of Circle is",a)
class Rectangle(shape):
    def disparea(a):
        print("Area of Rectangle is",a)
class Cube(shape):
    def disparea(a):
        print("Area of Cube is",a)

obj1=Rectangle
a=obj1.areaCalculator(8,3)
obj1.disparea(a)