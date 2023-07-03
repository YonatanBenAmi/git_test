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
        if board[row1][col1].color == '♚':
            print("1")
            if abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1:
                print("2")
                for row in range(1, len(board)):
                    for col in range(1, len(board[row])):
                        if board[row][col].color in black_characters:
                            print(board[row][col].color,board[row][col].check_steps(row, col, row2, col2, board))
                            if board[row][col].check_steps(row, col, row2, col2, board):
                                print(board[row][col],board[row][col].check_steps(row, col, row2, col2, board))
                                return False
                self._status_move = True
                return True
            return False
        elif board[row1][col1].color == '♔':
            if (abs(row1 - row2) == 1 and abs(col1 - col2) == 0) or (abs(row1 - row2) == 0 and abs(col1 - col2) == 1):
                for row in range(1, len(board)):
                    for col in range(1, len(board[row])):
                        if board[row][col].color in white_characters:
                            print(board[row][col].color, board[row][col].check_steps(row, col, row2, col2, board))
                            if board[row][col].check_steps(row, col, row2, col2, board):
                                print(board[row][col], board[row][col].check_steps(row, col, row2, col2, board))
                                return False
            self._status_move = True
            return True
        return False

    #
    # def king_threat(self,board):
    #     if board[][].color == '♚':
