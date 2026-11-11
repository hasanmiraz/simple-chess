from pieces.pieces import Pieces

class Cells:
    item: None|Pieces = None
    
    def __init__(self, x, y, item: None | Pieces=None) -> None:
        self.x = x
        self.y = y
        self.colour = self.set_colour(self.x, self.y)
        self.item = item
    
    def set_colour(self, x, y):
        if (x+y) %2 == 0:
            return "B"
        else:
            return "W"
    
    def set_cell(self, x, y, item=None):
        self.x = x
        self.y = y
        self.item = item
        
    def get_cell(self, x, y):
        return {
            "x": self.x,
            "y": self.y,
            "color": self.colour,
            "item": self.item,
        }
    
    def get_cells_compact(self):
        item_name = self.item.name if self.item is not None else "N"
        item_player = self.item.player if self.item is not None else "N"
        return (self.x, self.y, self.colour, item_name, item_player)
    