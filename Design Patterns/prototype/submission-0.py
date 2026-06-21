from abc import ABC, abstractmethod
import copy

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        anotherSquare = copy.copy(self)
        return anotherSquare

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        anotherRect = copy.copy(self)
        return anotherRect

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        res = []
        for shape in shapes:
            res.append(copy.copy(shape))
        
        return res
            
        
