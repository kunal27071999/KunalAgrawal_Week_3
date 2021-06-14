"""
4. Create below ctructure and understand the duck typing	
	Class Duck
		Create method talk with self and print Quack Quack
	Class Dog
		Create method talk with self and print Bow Bow
	Class Cat
		Create method talk with self and print Meow meow
	Class Goat
		Create method talk with self and print Myaah Myaah
	
	Create Declare function fun(object)
		call talk method of each object
	
Create list of the objects containing object of each class and iterate on it. Call the function fun for each object.

"""
class Duck:
    def talk(self):
        print("Quack Quack")

class Dog:
    def talk(self):
        print("Bow Bow")

class Cat:
    def talk(self):
        print("Meow Meow")


d = Duck()
do = Dog()
c = Cat()

d.talk()
do.talk()
c.talk()