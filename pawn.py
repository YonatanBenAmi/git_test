class Pawn:
    def __init__(self, row, col, unicode):
        self.row = row
        self.col = col
        self.unicode = unicode

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_unicode(self):
        return self.unicode

