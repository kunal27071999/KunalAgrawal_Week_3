"""

26. Create an interface as ShapeDetails which extends the ABC and declare below abstract methods
	- calculateArea
	- displayNumOfSides
	- displayArea 
	- Create Class Circle, implement the interface in it, provide the implementation to interface methods
	- Get the classname as input from console, initialize the obejct and call all the methods declared in that Class

"""

import zope.interface
class ShapeDetails(zope.interface.Interface):
    def calArea(self):
        pass
    def sides(self):
        pass
    def Area(self):
        pass
class Circle:
    def calArea(self,r):
        return (3.14*r*r)
    def sides(self):
        print("Infinite")
    def Area(self,r):
        print(self.calArea(r))

s=Circle()
s.sides()
s.Area(3)