from classsim import ChessCharacter


class Knight(ChessCharacter):

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
        if d_row == 1 and d_col == 2 or d_row == 2 and d_col == 1:
            return True
        return False


