"""
16. Method overriding: Create Class Shape, define areaCalculator method to calculate area, use Variable arguments to take arguments. Define displayArea method which will print the name and area of shape.
Create classes : Circle, Rectangle and Cube, inherit the Shape class and declare their own displayArea method.
Create object of each class and call areaCalculator method and display method to print the calculated area and name of the shape.

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