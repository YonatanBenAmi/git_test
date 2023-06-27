from classsim import ChessCharacter
from point import Point
class Pawn(ChessCharacter):
    def __init__(self,color="", point=Point(), promotion=False, status_move=False):
        super().__init__(color, point)
        self._promotion = promotion
        self._status_move = status_move

    def __str__(self):
        return self.color

    # def check_steps(self, row1, col1, row2, col2, board):
    #     black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
    #     white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']
    #
    #     if board[row1][col1].color in white_characters and board[row2][col2].color in white_characters:
    #         return False
    #     if board[row1][col1].color in black_characters and board[row2][col2].color in black_characters:
    #         return False
    #     if abs(row1 - row2) == 0 and abs(col1 - col2) == 1 or \
    #             abs(row1 - row2) == 1 and abs(col1 - col2) == 1 and board[row2][col2].color
