class ChessBoard:

    def __init__(self):
        self._pisces = []
        self._board = []

    def create_new_board(self):
        from pawn import Pawn

        king_black, king_white = chr(0x2654), chr(0x265A)
        queen_black, queen_white = chr(0x2655), chr(0x265B)
        rook_black, rook_white = chr(0x2656), chr(0x265C)
        knight_black, knight_white = chr(0x2658), chr(0x265E)
        pawn_black, pawn_white = chr(0x2659), chr(0x265F)
        bishop_black, bishop_white = chr(0x2657), chr(0x265D)
        tav = chr(11055)

        array = [
                    [' ', '１', '２', '３', '４', '５', '６', '７', '８'],
                    ['A', tav, tav, tav, tav, tav, tav, tav, tav],
                    ['B', tav, tav, tav, tav, tav, tav, tav, tav],
                    ['C', tav, tav, tav, tav, tav, tav, tav, tav],
                    ['D', tav, tav, tav, tav, tav, tav, tav, tav],
                    ['E', tav, tav, tav, tav, tav, tav, tav, tav],
                    ['F', tav, tav, tav, tav, tav, tav, tav, tav],
                    ['G', tav, tav, tav, tav, tav, tav, tav, tav],
                    ['H', tav, tav, tav, tav, tav, tav, tav, tav]]

        dic_line = (2, 7)
        character = chr(0x2659)

        for line in dic_line:
            for column in range(1, 9):
                pawn = Pawn(line, column, character)
                row = pawn.get_row()
                col = pawn.get_col()
                array[row][col] = character
            character = chr(0x265F)
            self._board = array
        return self._board

    def get_board(self):
        return self._board

    def print_board(self):
        for i in self._board:
            print(*i)




