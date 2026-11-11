from board.cells import Cells
from pieces.pawns import Pawns

class Board:
    def __init__(self) -> None:
        pass
    
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
        print("-"*((14*8)+1))
        
        for h in range(self.height-1, -1, -1):
            print("| ", end="")
            for w in range(self.width):
                print(self.cells[w][h].get_cells_compact(), end=" | ")
            
            print("\n", end="")
            print("-"*((26*8)+1))
