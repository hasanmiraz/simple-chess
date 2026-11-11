from board.board import Board
from pieces.pawns import Pawns

def main() -> None:
    chess_board = Board()
    chess_board.process_board()
    chess_board.draw_board()
    
if __name__ == "__main__":
    main()