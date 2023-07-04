from pawn import Pawn
from king import King
from knight import Knight
from queen import Queen
from bishop import Bishop
from rook import Rook
from tav import Tav

class Chess_board:

    def __init__(self,board=[]):

        self.board = board



    def create_new_board(self):
        tav = Tav(chr(11055))
        self.board =  [[' ', '１', '２', '３', '４', '５', '６', '７', '８']]
        iner_list = []
        letter = "A"
        for row in range(1, 9):
            iner_list.append(letter)
            for col in range(1,9):
               iner_list.append(tav)
            self.board.append(iner_list)
            iner_list = []
            letter = ord(letter)
            letter+=1
            letter = chr(letter)


    def print_board(self):
        for col in range(0,9):
            print(*self.board[col])
        print()

    def fill_it_with_pawons(self):
        # character_pawan = chr(0x2659)
        for row in range(2,8,5):
            for col in range(1, 9):
                if row == 2:
                    pawn = Pawn(chr(0x2659),(row,col))
                    self.board[row][col] = pawn
                else:
                    pawn = Pawn(chr(0x265F), (row, col))
                    self.board[row][col] = pawn




    def fill_in_all_chrecters(self):
        king_black, king_white = King('♔'), King('♚')
        queen_black, queen_white = Queen('♕'), Queen('♛')
        rook_black, rook_white = Rook(chr(0x2656)), Rook(chr(0x265C))
        knight_black, knight_white = Knight(chr(0x2658)), Knight(chr(0x265E))
        bishop_black, bishop_white = Bishop(chr(0x2657)), Bishop(chr(0x265D))
        self.board[1][1],self.board[1][2],self.board[1][3],self.board[1][4],self.board[1][5],self.board[1][6],self.board[1][7],self.board[1][8] = \
            rook_black, bishop_black, knight_black,queen_black,king_black,knight_black,bishop_black,rook_black

        self.board[8][1], self.board[8][2], self.board[8][3], self.board[8][4], self.board[8][5], self.board[8][6], \
        self.board[8][7], self.board[8][8] = \
            rook_white, bishop_white, knight_white, queen_white, king_white, knight_white, bishop_white, rook_white

    def fill_what_you_want(self):
        king_black, king_white = King('♔'), King('♚')
        queen_black, queen_white = Queen('♕'), Queen('♛')
        rook_black, rook_white = Rook(chr(0x2656)), Rook(chr(0x265C))
        knight_black, knight_white = Knight(chr(0x2658)), Knight(chr(0x265E))
        bishop_black, bishop_white = Bishop(chr(0x2657)), Bishop(chr(0x265D))
        self.board[2][1], self.board[2][2], self.board[2][3], self.board[2][4], self.board[2][5], self.board[2][6], \
        self.board[2][7], self.board[2][8] =  Pawn(chr(0x265F), (0, 0)),Pawn(chr(0x265F), (0, 0)),Pawn(chr(0x265F), (0, 0)),Pawn(chr(0x265F), (0, 0)),Pawn(chr(0x265F), (0, 0)),Pawn(chr(0x265F), (0, 0)),Pawn(chr(0x265F), (0, 0)),Pawn(chr(0x265F), (0, 0))
        self.board[7][1], self.board[7][2], self.board[7][3], self.board[7][4], self.board[7][5], self.board[7][6], \
            self.board[7][7], self.board[7][8] = Pawn(chr(0x2659),(0,0)),Pawn(chr(0x2659),(0,0)),Pawn(chr(0x2659),(0,0)),Pawn(chr(0x2659),(0,0)),Pawn(chr(0x2659),(0,0)),Pawn(chr(0x2659),(0,0)),Pawn(chr(0x2659),(0,0)),Pawn(chr(0x2659),(0,0))

    def create_new_board_game_start(self):
        tav = Tav(chr(11055))
        self.board = [[' ', '１', '２', '３', '４', '５', '６', '７', '８']]
        iner_list = []
        letter = "A"
        for row in range(1, 9):
            iner_list.append(letter)
            for col in range(1, 9):
                iner_list.append(tav)
            self.board.append(iner_list)
            iner_list = []
            letter = ord(letter)
            letter += 1
            letter = chr(letter)

        for row in range(2, 8, 5):
            for col in range(1, 9):
                if row == 2:
                    pawn = Pawn(chr(0x2659), (row, col))
                    self.board[row][col] = pawn
                else:
                    pawn = Pawn(chr(0x265F), (row, col))
                    self.board[row][col] = pawn

        king_black, king_white = King('♔'), King('♚')
        queen_black, queen_white = Queen('♕'), Queen('♛')
        rook_black, rook_white = Rook(chr(0x2656)), Rook(chr(0x265C))
        knight_black, knight_white = Knight(chr(0x2658)), Knight(chr(0x265E))
        bishop_black, bishop_white = Bishop(chr(0x2657)), Bishop(chr(0x265D))
        self.board[1][1], self.board[1][2], self.board[1][3], self.board[1][4], self.board[1][5], self.board[1][6], \
        self.board[1][7], self.board[1][8] = \
            rook_black, knight_black,bishop_black , queen_black, king_black, bishop_black, knight_black, rook_black

        self.board[8][1], self.board[8][2], self.board[8][3], self.board[8][4], self.board[8][5], self.board[8][6], \
            self.board[8][7], self.board[8][8] = \
            rook_white, knight_white, bishop_white, queen_white, king_white, bishop_white, knight_white, rook_white



# def main():


# a = Chess_board()
# a.create_new_board()
# a.print_board()
# a.fill_it_with_pawons()
# a.print_board()
#








#     def __init__(self):
#         self._pices = []
#         self._board = []
#     def create_new_board(self):
#         from pawn import Pawn
#
#         king_black, king_white = chr(0x2654), chr(0x265A)
#         queen_black, queen_white = chr(0x2655), chr(0x265B)
#         rook_black, rook_white = chr(0x2656), chr(0x265C)
#         knight_black, knight_white = chr(0x2658), chr(0x265E)
#         pawn_black, pawn_white = chr(0x2659), chr(0x265F)
#         bishop_black, bishop_white = chr(0x2657), chr(0x265D)
#         tav = chr(11055)
#
#         array = [   [' ', '１', '２', '３', '４', '５', '６', '７', '８'],
#                     ['A', tav, tav, tav, tav, tav, tav, tav, tav],
#                     ['B', tav, tav, tav, tav, tav, tav, tav, tav],
#                     ['C', tav, tav, tav, tav, tav, tav, tav, tav],
#                     ['D', tav, tav, tav, tav, tav, tav, tav, tav],
#                     ['E', tav, tav, tav, tav, tav, tav, tav, tav],
#                     ['F', tav, tav, tav, tav, tav, tav, tav, tav],
#                     ['G', tav, tav, tav, tav, tav, tav, tav, tav],
#                     ['H', tav, tav, tav, tav, tav, tav, tav, tav]]
#
#         dic_line = (2, 7)
#         character = chr(0x2659)
#
#         for line in dic_line:
#             for column in range(1, 9):
#                 pawn = Pawn(line, column, character)
#                 row = pawn.get_row()
#                 col = pawn.get_col()
#                 array[row][col] = character
#             character = chr(0x265F)
#             self._board= array
#         return self._board
#
#
#     def get_board(self):
#         return self._board
#     def print_board(self):
#         for i in self._board:
#             print(*i)
#
#
#
#
# # array = [   [' ', '１', '２', '３', '４', '５', '６', '７', '８'],
# #         #             ['A', tav, tav, tav, tav, tav, tav, tav, tav],
#         #             ['B', tav, tav, tav, tav, tav, tav, tav, tav],
#         #             ['C', tav, tav, tav, tav, tav, tav, tav, tav],
#         #             ['D', tav, tav, tav, tav, tav, tav, tav, tav],
#         #             ['E', tav, tav, tav, tav, tav, tav, tav, tav],
#         #             ['F', tav, tav, tav, tav, tav, tav, tav, tav],
#         #             ['G', tav, tav, tav, tav, tav, tav, tav, tav],
#         #             ['H', tav, tav, tav, tav, tav, tav, tav, tav]]
