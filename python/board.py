from cells import Cells
from pieces.pawns import Pawns

class Board:
    def __init__(self) -> None:
        height = 8
        width = 8
        height_label = "number"
        width_label = "letter"
        cells = None
    
    def set_initial_pieces(self, piece):
        pawn1 = Pawns(0,1,True, "W")
    
    def process_board(self, height=8, width=8) -> None:
        self.height = height
        self.width = width
        self.cells =[]
        for h in range(height):
            row_cells = []
            for w in range(width):
                row_cells.append(Cells(w,h))
            self.cells.append(row_cells)
                    
    def draw_board(self):
        for h in range(self.height-1, -1, -1):
            for w in range(self.width):
                print(self.cells[w][h].get_cells_compact(), end="")
            print("\n")
