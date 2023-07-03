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
#
# class King(ChessCharacter):
#     def __init__(self, color="", point=Point(), status_move=False):
#         super().__init__(color, point)
#         self._status_move = status_move
#
#     def __str__(self):
#         return self.color
#
#     def can_castle(self, row1, col1, row2, col2, board):
#         # התנאים הנדרשים לביצוע הצרחה
#         if (
#             not self._status_move and
#             not board[row2][col2]._status_move and
#             self.point.row == row1 and
#             self.point.col == col1 and
#             abs(col1 - col2) == 2 and
#             board[row1][col1 + int((col2 - col1) / 2)].color == '' and
#             board[row1][col1 + int((col2 - col1) / 2)].can_castle and
#             all(board[row1][min(col1, col2) + i].color == '' for i in range(1, abs(col1 - col2)))
#         ):
#             return True
#         return False
#
#     def perform_castling(self, row1, col1, row2, col2, board):
#         # ביצוע הצרחה
#         king_col = min(col1, col2)
#         rook_col = max(col1, col2)
#         board[row1][king_col], board[row2][rook_col] = board[row2][rook_col], board[row1][king_col]
#         board[row1][king_col + 1], board[row2][rook_col - 1] = board[row2][rook_col - 1], board[row1][king_col + 1]
#
#     def check_steps(self, row1, col1, row2, col2, board):
#         black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
#         white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']
#
#         if board[row1][col1].color in white_characters and board[row2][col2].color in white_characters:
#             print('same group')
#             return False
#         if board[row1][col1].color in black_characters and board[row2][col2].color in black_characters:
#             print('same group')
#             return False
#         if self.can_castle(row1, col1, row2, col2, board):
#             self.perform_castling(row1, col1, row2, col2, board)
#             self._status_move = True
#             print('castling')
#             return True
#         if abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1:
#             self._status_move = True
#             print('ok')
#             self.status_move = True
#             return True
#         print('not ok')
#         return False