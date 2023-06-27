from classsim import ChessCharacter
from point import point
class Pawn(ChessCharacter):
    def __init__(self,color="", point=point(), promotion=False, status_move=False):
        super().__init__(color, point)
        self._promotion = promotion
        self._status_move = status_move

    def __str__(self):
        return self.color
    def steps(self, array ,user_start):
        for row in range(1,9):
            for col in range(1,9):
                if array[row][col] == type(Pawn) and (row,col) == user_start:
                    a = array[row][col]
                    break
            break
