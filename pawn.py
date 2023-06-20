from classsim import ChessCharacter


class Pawn(ChessCharacter):
    def __init__(self, promotion):
        self.__promotion = promotion

    def steps(self):
        pass

    def castling(self):
        pass
