from classsim import ChessCharacter
from point import Point
from  tav import Tav
from  queen import Queen
from knight import Knight
from rook import Rook
from bishop import Bishop
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
            #jump two condition
            if board[row2][col2].color == chr(11055) and row1 - row2 == -2 and col1 - col2 == 0 and self._status_move == False\
                    and board[3][col1].color == chr(11055):
                self._status_move = True
                return True
            #eat condition
            if board[row2][col2].color != chr(11055) and row1 - row2 == -1 and abs(col1 -col2) == 1:
                if row2 == 8:
                    blak_prmotion = [Queen('♕'), Knight(chr(0x2658)), Rook(chr(0x2656)), Bishop(chr(0x2657))]
                    for i in range(4):
                        print(i + 1, blak_prmotion[i])
                    choise = int(input("choose premotion"))
                    board[row1][col1] = blak_prmotion[choise-1]
                return True
            #walk condition
            elif row1 - row2 == -1 and col1 - col2 == 0 and board[row2][col2].color == chr(11055):
                if row2 == 8:
                    blak_prmotion = [Queen, Knight, Rook, Bishop]
                    for i in range(4):
                        print(i + 1, blak_prmotion[i])
                    choise = int(input("choose premotion"))
                    board[row1][col1] = blak_prmotion[choise - 1]
                return True
        #condition for white
        elif board[row1][col1].color == chr(0x265F):
            # jump two condition
            if board[row2][col2].color == chr(11055) and row1 - row2 == 2 and col1 - col2 == 0 and self._status_move == False\
                    and board[6][col1].color == chr(11055):
                self._status_move = True
                return True
            # eat condition
            if board[row2][col2].color != chr(11055) and row1 - row2 == 1 and abs(col1 - col2) == 1:
                if row2 == 1:
                    blak_prmotion = [Queen('♕'), Knight(chr(0x2658)), Rook(chr(0x2656)), Bishop(chr(0x2657))]
                    for i in range(4):
                        print(i + 1, blak_prmotion[i])
                    choise = int(input("choose premotion"))
                    board[row1][col1] = blak_prmotion[choise - 1]
                return True
            # walk condition
            elif row1 - row2 == 1 and col1 - col2 == 0 and board[row2][col2].color == chr(11055):
                if row2 == 1:
                    white_prmotion = [Queen('♛'), Knight(chr(0x265E)), Rook(chr(0x265C)), Bishop(chr(0x265D))]
                    for i in range(4):
                        print(i + 1, white_prmotion[i])
                    choise = int(input("choose premotion"))
                    board[row1][col1] = white_prmotion[choise - 1]
                return True

