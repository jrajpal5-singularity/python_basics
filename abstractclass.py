# class Shape:
#     def area(self): pass
#     def perimeter(self): pass
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.__side = side
#
#
# shape = Shape()
# Suppose we don't want that class shape couldn't be called as is done in this line.
# for this abstract class function is used
# Abstract class is method to restrict classes not to be called.
# in python there is no explicit abstract class but there is built-in module for that

from abc import ABC, abstractmethod  # Abstract based Classes


class Shape(ABC):
    @abstractmethod  # abstractmethod is decorator method which must be implemented in subclass as abstract
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass  # perimeter and area method are abstract methods


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


square = Square(5)
print(square.perimeter())
print(square.area())
