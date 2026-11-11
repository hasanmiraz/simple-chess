from controller import Controller
from player.player import Player
from board.board import Board 
from pieces.pawns import Pawns

def main() -> None:
    chess_controller = Controller()
    
    chess_board = Board()
    player_1 = Player(colour="W", active=True, peices=None)
    player_2 = Player(colour="B", active=False, peices=None)
    
    chess_controller.set_game(board=chess_board, player1=player_1, player2=player_2)
    
    
if __name__ == "__main__":
    main()