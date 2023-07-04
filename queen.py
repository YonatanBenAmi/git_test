from classsim import ChessCharacter


class Queen(ChessCharacter):

    def __str__(self):
        return self.color

    def check_steps(self, row1, col1, row2, col2, board):
        super().check_steps(row1, col1, row2, col2, board)

        d_row = abs(row1 - row2)
        d_col = abs(col1 - col2)

        if d_row == d_col:
            jmp_col = 1 if col1 < col2 else -1
            jmp_row = 1 if row1 < row2 else -1

            row = row1 + jmp_row
            col = col1 + jmp_col

            while row != row2 and col != col2:
                if board[row][col].color != chr(11055):
                    return False
                row += jmp_row
                col += jmp_col
        elif d_row == 0 and d_col > 0:
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
        return False
