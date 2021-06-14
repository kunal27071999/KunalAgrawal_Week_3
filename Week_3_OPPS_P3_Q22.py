"""
22. Create class Animal and declare the abstract method talk in it.
Create class Dog, Duck, Cat and Goat. Inherit the class Animal and provide the implementation to talk method.
Talk method will print the voice of an animal.

"""

from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def talk(self):
        pass
class Dog(Animal):
    def talk(self):
        print("Bow Bow")
class Duck(Animal):
    def talk(self):
        print("Quack Quack")
class Cat(Animal):
    def talk(self):
        print("Meo Meo")
class Goat(Animal):
    def talk(self):
        print("Meh meh")

ob=Goat()
ob.talk()
