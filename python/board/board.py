from board.cells import Cells
from pieces.pawns import Pawns

class Board:
    def __init__(self):
        pass
    
    def process_board(self, height=8, width=8, peices=None) -> None:
        self.height = height
        self.width = width
        self.cells =[]
        for h in range(height):
            row_cells = []
            for w in range(width):
                peice = None
                
                if peices is not None:
                    for p in peices:
                        if p.x==w and p.y==h:
                            peice = p
                            break
                        else:
                            peice = None
                
                row_cells.append(Cells(x=w, y=h, item=peice))
           
            self.cells.append(row_cells)
    
    def draw_board(self):
        str_len = len(f"{self.cells[0][0].get_cells_compact()} | ")
        print("-"*((str_len*8)+1))
        
        for h in range(self.height-1, -1, -1):
            print("| ", end="")
            for w in range(self.width):
                print(self.cells[w][h].get_cells_compact(), end=" | ")
            
            print("\n", end="")
            print("-"*((str_len*8)+1))
