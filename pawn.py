from classsim import ChessCharacter
class Pawn(ChessCharacter):
    def __init__(self,row, col, unicode, promotion=False, status_move=False):
        super().__init__(row, col, unicode)
        self._promotion = promotion
        self._status_move = status_move


