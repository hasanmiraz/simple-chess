from pieces.pawns import Pawns

class Board:
    def __init__(self) -> None:
        height = 8
        width = 8
        height_label = "number"
        width_label = "letter"
    
    def cell(self, x=0, y=0, item=None) -> str:
        if((x+y) %2 == 0):
            return f"B, {x,y}"
        else:
            return f"W, {x,y}"
    
    def set_initial_pawnd(self):
        for i in range (8):
            
    
    def set_initial_pieces(self, piece):
        pawn1 = Pawns(0,1,True, "W")
    
    def draw_board(self, height=8, width=8) -> None:
        self.height = height
        self.width = width
        
        for h in range(height, -1, -1):
            for w in range(width):
                print(f" | {self.cell(w,h)}| ", end="")
            
            print("\n")
            print("-" * (len(f" | ({h,w}) | ") * self.width))
            
            