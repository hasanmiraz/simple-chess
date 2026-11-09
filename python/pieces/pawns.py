from pieces.pieces import Pieces

class Pawns(Pieces):
    def __init__(self, x, y, state, colour):
        super().__init__(x, y, state, colour)
    
    def set_position(self, x, y):
        return super().set_position(x, y)
    
    def get_name(self):
        return "P"
    