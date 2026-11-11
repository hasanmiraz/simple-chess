from player.player import Player
from board.board import Board
from pieces.pawns import Pawns

class Controller:
    def __init__(self):
        pass
    
    def set_game(self, board: Board, player1: Player, player2: Player):
        player1.peices = self.get_initial_peice(player1.colour)
        player2.peices = self.get_initial_peice(player2.colour)
        
        peices = player1.peices + player2.peices
        
        board.process_board(peices=peices)
        board.draw_board()
        
    def get_initial_peice(self, color):
        pawn_place = 1 if color=="W" else 6
        peices = []
        for i in range(8):
            obj = Pawns(pawn_place, i, True, color)
            peices.append(obj)
            
        return peices
    
            
    