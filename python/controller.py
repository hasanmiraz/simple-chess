from board import Board

from pieces.pawns import Pawns

class Controller:
    def __init__(self) -> None:
        self.board = Board()
        self.pawnsW = []
        self.pawnsB = []
        for i in range(8):
            obj1 = Pawns(i, 1, True, "W")
            obj2 = Pawns(i, 7, True, "B")
            self.pawnsW.append(obj1)
            self.pawnsB.append(obj2)
            
    