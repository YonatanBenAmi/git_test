from classsim import ChessCharacter
from point import Point


class King(ChessCharacter):
    def __init__(self, color="", point=Point(), status_move=False):
        super().__init__(color, point)
        self._status_move = status_move

    def __str__(self):
        return self.color

    def check_steps(self, row1, col1, row2, col2, board):
        black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
        white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']

        if board[row1][col1].color in white_characters and board[row2][col2].color in white_characters:
            print('same group')
            return False
        if board[row1][col1].color in black_characters and board[row2][col2].color in black_characters:
            print('same group')
            return False
        if abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1:
            self._status_move = True

            print('ok')
            self.status_move = True
            return True
        print('not ok')
        return False

    def if_king_dead(self):
        pass

