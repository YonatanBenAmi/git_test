from classsim import ChessCharacter


class Pawn(ChessCharacter):
    def __init__(self,row, col, unicode, promotion=False, status_move=False):
        super().__init__(row, col, unicode)
        self._promotion = promotion
        self._status_move = status_move

    def steps(self, row1, col1, row2, col2):
        return abs(row1 - row2) > 0 and abs(col1 - col2) == 0

    def check_mov(self, row1, row2, col1, col2, array):
        self.row1 = row1
        self.row2 = row2
        self.col1 = col1
        self.col2 = col2
        array[row1][col1] = chr(11055)
        array[row2][col2] = chr(0x2659)


        for i in array:
            print(*i)


