"""
20. Write note on 
	- Abstract method, @abstractmethod and abc
	- Abstract class
	- Interface
	- public, private and protected members 

"""
"""
The collections module has some concrete classes that derive from ABCs; these can, of course, be further derived. In addition, the collections.abc submodule has some ABCs that can be used to test whether a class or instance provides a particular interface, for example, if it is hashable or if it is a mapping.

This module provides the metaclass ABCMeta for defining ABCs and a helper class ABC to alternatively define ABCs through inheritance:

class abc.ABC
A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from ABC avoiding sometimes confusing metaclass usage, for example:

from abc import ABC

class MyABC(ABC):
    pass
Note that the type of ABC is still ABCMeta, therefore inheriting from ABC requires the usual precautions regarding metaclass usage, as multiple inheritance may lead to metaclass conflicts. One may also define an abstract base class by passing the metaclass keyword and using ABCMeta directly, for example:

from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass

"""