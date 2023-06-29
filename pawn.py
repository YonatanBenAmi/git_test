from classsim import ChessCharacter
from point import Point
from  tav import Tav
class Pawn(ChessCharacter):
    def __init__(self,color="", point=Point(), promotion=False, status_move=False):
        super().__init__(color, point)
        self._promotion = promotion
        self._status_move = status_move


    def __str__(self):
        return self.color

    def check_steps(self, row1, col1, row2, col2, board):
        black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
        white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']

        if board[row1][col1].color in white_characters and board[row2][col2].color in white_characters:
            return False
        if board[row1][col1].color in black_characters and board[row2][col2].color in black_characters:
            return False

        # condition for black
        if board[row1][col1].color == chr(0x2659):
            if board[row2][col2].color == chr(11055) and row1 - row2 == -2 and col1 - col2 == 0 and self._status_move == False:
                self._status_move = True
                return True
            if board[row2][col2].color != chr(11055) and row1 - row2 == -1 and abs(col1 -col2) == 1:
                return True
            elif row1 - row2 == -1 and col1 - col2 == 0 and board[row2][col2].color == chr(11055):
                return True
        #condition for white
        elif board[row1][col1].color == chr(0x265F):
            if board[row2][col2].color == chr(11055) and row1 - row2 == 2 and col1 - col2 == 0 and self._status_move == False:
                self._status_move = True
                return True
            if board[row2][col2].color != chr(11055) and row1 - row2 == 1 and abs(col1 - col2) == 1:
                return True
            elif row1 - row2 == 1 and col1 - col2 == 0 and board[row2][col2].color == chr(11055):
                return True

