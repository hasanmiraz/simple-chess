from abc import ABC, abstractmethod

class Pieces(ABC):
    def __init__(self, x=0, y=0, state=True, colour=None):
        self.x = x
        self.y = y
        self.state = state
        self.colour = colour
    
    @abstractmethod
    def set_position(self, x, y):
        pass
    
    # @abstractmethod
    # def get_position(self):
    #     pass
    
    # @abstractmethod
    # def move(self):
    #     pass