from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    

class Object:
    def __init__(self, id, capacity, color,bin_id=None):
        self.id=id
        self.capacity=capacity
        self.color=color
        self.bin_id=None
        pass