from classsim import ChessCharacter


class Bishop(ChessCharacter):
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

        if d_row == d_col:
            if col1 > col2:
                jmp_col = -1
            else:
                jmp_col = 1

            if row1 > row2:
                jmp_row = -1
            else:
                jmp_row = 1

            steps_row = row1 + jmp_row
            steps_col = col1 + jmp_col

            while steps_row != row2 and steps_col != col2:
                if board[steps_row][steps_col].color != chr(11055):
                    return False
                steps_row += jmp_row
                steps_col += jmp_col
            return True
        return False
