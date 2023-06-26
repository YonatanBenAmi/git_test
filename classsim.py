
class ChessCharacter:
        def __init__(self, row=0, col=0, unicode=0):
                self.row = row
                self.col = col
                self.unicode = unicode

        def get_row(self):
                return self.row

        def get_col(self):
                return self.col

        def get_unicode(self):
                return self.unicode

        def check_steps(self, row, col):
                self.row = row
                self.col = col

                if (self.row > 8 or self.row < 1) and (self.col > 8 or self.col < 1):
                        return False
                return True

