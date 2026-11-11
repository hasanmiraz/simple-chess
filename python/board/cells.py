class Cells:
    def __init__(self, x, y, item=None) -> None:
        self.x = x
        self.y = y
        self.colour = self.set_colour(self.x, self.y)
        self.item = item
    
    def set_colour(self, x, y):
        if (x+y) %2 == 0:
            return "B"
        else:
            return "W"
    
    def set_cell(self, x, y, item=None, player=None):
        self.x = x
        self.y = y
        self.item = item
        self.player = player
        
    def get_cell(self, x, y):
        return {
            "x": self.x,
            "y": self.y,
            "color": self.colour,
            "item": self.item,
            "player": self.player
        }
    
    def get_cells_compact(self):
        item_name = self.item.name if self.item is not None else None
        item_player = self.item.player if self.item is not None else None
        return (self.x, self.y, self.colour, item_name, item_player)
    