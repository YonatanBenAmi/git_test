from classsim import ChessCharacter
from tav import  Tav

class Rook(ChessCharacter):
    def __str__(self):
        return self.color

    def check_steps(self, row1, col1, row2, col2, board):
        black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
        white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']

        if board[row1][col1].color in white_characters and board[row2][col2].color in white_characters:
            return False
        if board[row1][col1].color in black_characters and board[row2][col2].color in black_characters:
            return False
        d_row = abs(row1 - row2)
        d_col = abs(col1 - col2)
        jmp_steps = 0

        if d_row == 0 and d_col > 0:
            if col1 > col2:
                jmp_steps = -1
            else:
                jmp_steps = 1
            for check in range(col1 + jmp_steps, col2, jmp_steps):
                if board[row1][check].color != chr(11055):
                    return False
            return True
        elif d_col == 0 and d_row > 0:
            if row1 > row2:
                jmp_steps = -1
            else:
                jmp_steps = 1
            for check in range(row1 + jmp_steps, row2, jmp_steps):
                if board[check][col1].color != chr(11055):
                    return False

            return True












#     def __init__(self, movement_status=True):
#         self.__movement_status = movement_status
#
#     def steps(self, row1, row2, col1, col2):
#         self.row1 = row1
#         self.row2 = row2
#         self.col1 = col1
#         self.col2 = col2
#
#         return self.row1 == self.row2 or self.col1 == self.col2
#
#     def check_steps(self, num):
#         self.num = num
#         if self.num > 7 or self.num < 0:
#             return False
#         return True
#
#     def castling(self):
#         pass
#
#
# a = Rook()
# row1 = int(input("Enter row1: "))
# while not a.check_steps(row1):
#     row1 = int(input("Enter row1: "))
#
# col1 = int(input("Enter col1: "))
# while not a.check_steps(col1):
#     col1 = int(input("Enter col1: "))
#
# print('Current player position - (row, column):', (row1, col1))
#
# row2 = int(input("Enter row2: "))
# while not a.check_steps(row2):
#     row2 = int(input("Enter row2: "))
#
# col2 = int(input("Enter col2: "))
# while not a.check_steps(col2):
#     col2 = int(input("Enter col2: "))
# print('Position the player wants to move - (row, column):', (row2, col2))
#
# print(a.steps(row1, row2, col1, col2))
