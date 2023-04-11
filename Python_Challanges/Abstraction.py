from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of a shape
        """
        pass
    
    def perimeter(self):
        """
        Method to calculate the perimeter of a shape
        """
        pass

class Rectangle(Shape):
    """
    Concrete class that implements the Shape abstract class for rectangles
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        """
        Implementation of the area method for rectangles
        """
        return self.length * self.width
    
    def perimeter(self):
        """
        Implementation of the perimeter method for rectangles
        """
        return 2 * (self.length + self.width)

# create an object of the Rectangle class
r = Rectangle(5, 10)

# call the area method of the Rectangle object
print("The area of the rectangle is:", r.area())

# call the perimeter method of the Rectangle object
print("The perimeter of the rectangle is:", r.perimeter())

