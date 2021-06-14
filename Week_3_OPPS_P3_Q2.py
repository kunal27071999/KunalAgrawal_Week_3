"""
2. What is duck typing philosophy of python
"""

"""
Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc.
where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do
not check types at all. Instead, we check for the presence of a given method or attribute.

The name Duck Typing comes from the phrase:

“If it looks like a duck and quacks like a duck, it’s a duck”

Example:


# Python program to demonstrate
# duck typing
  
class Specialstring:
    def __len__(self):
        return 21
  
# Driver's code
if __name__ == "__main__":
  
    string = Specialstring()
    print(len(string))
"""