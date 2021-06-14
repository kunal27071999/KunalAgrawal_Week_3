"""
8. Create class Book init it using number of pages. Create two objects of the class book with num pages as 100 and 200 respectively. Tey to perform the + operation on those objects.

"""
class Book:
    def __init__(self,a):
        self.a=a
    def __add__(self, o):
        return self.a+o.a

pg1=Book(100)
pg2=Book(200)
print(pg1+pg2)