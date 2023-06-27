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
        drow = abs(row1 - row2)
        dcol = abs(col1 - col2)
        if drow == 1 and dcol == 2 or drow == 2 and dcol == 1:
            return True
        return False