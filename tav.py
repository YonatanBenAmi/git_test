from classsim import ChessCharacter
from point import Point


class Tav(ChessCharacter):

    def __str__(self):
        return self.color

    def check_steps(self, row1, col1, row2, col2, board):
        return False