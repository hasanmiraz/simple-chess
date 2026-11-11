from pieces.pieces import Pieces

class Pawns(Pieces):
    name = "P"
    player = "N"
    
    def __init__(self, x, y, state, colour):
        super().__init__(x=x, y=y, name=self.get_name(), state=state, colour=colour)
        self.player = colour
    
    def set_position(self, x, y):
        return super().set_position(x, y)
    
    def get_name(self):
        return self.name
    