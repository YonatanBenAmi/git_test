from chess_bord import Chess_board
from tav import Tav



class Players:
    def __init__(self,chess_board=Chess_board(), turn="white", map_squrs={}):
        self.chess_board = chess_board
        self.map_squrs = map_squrs
        self.turn = turn

    def map_location(self):
        self.map_squrs = {}
        letter = "a"
        for row in range(1, 9):
            for col in range(1, 9):
                self.map_squrs[letter+str(col)] = (row, col)
            letter = ord(letter)
            letter += 1
            letter = chr(letter)

    def move_chess_board(self):
        while True:
            a = input("pick from square ")
            if a in self.map_squrs:
                b = input("pick to square ")
                if b in self.map_squrs:
                    # print("wright corrdinations")
                    a = list(self.map_squrs[a])
                    b = list(self.map_squrs[b])
                    black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
                    white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']
                    if (self.turn == "white" and self.chess_board[a[0]][a[1]].color in white_characters)\
                         or (self.turn == "black" and self.chess_board[a[0]][a[1]].color in black_characters):
                            if  not self.king_threat():
                                if self.chess_board[a[0]][a[1]].check_steps(a[0], a[1], b[0], b[1], self.chess_board):
                                    self.chess_board[int(b[0])][int(b[1])] = self.chess_board[int(a[0])][int(a[1])]
                                    self.chess_board[int(a[0])][int(a[1])] = Tav(chr(11055))
                                    if self.turn == "white":
                                        self.turn = "black"
                                        break
                                    elif self.turn == "black":
                                        self.turn = "white"
                                        break
                                else:
                                     print("you cant perform this action")


                            else:
                                print("your king is in threat")
                                if self.chess_board[a[0]][a[1]].check_steps(a[0], a[1], b[0], b[1], self.chess_board) and self.king_threat() == True:
                                    c = self.chess_board[int(b[0])][int(b[1])]
                                    self.chess_board[int(b[0])][int(b[1])] = self.chess_board[int(a[0])][int(a[1])]
                                    self.chess_board[int(a[0])][int(a[1])] = Tav(chr(11055))
                                    if self.king_threat() == False:
                                        if self.turn == "white":
                                            self.turn = "black"
                                            break
                                        else:
                                            self.turn = "white"
                                            break
                                    else:
                                        print("your king still in threat")
                                        self.chess_board[int(a[0])][int(a[1])] =  self.chess_board[int(b[0])][int(b[1])]
                                        self.chess_board[int(b[0])][int(b[1])] = c
                    else:
                        print("pick your own tools ")


    def print_chess_board(self):
        for col in range(0, 9):
            print(*self.chess_board[col])
        print()

    def is_end_game(self):
        pass

    def king_threat(self):
        # black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
        # white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']
        #
        # if self.turn == "white":
        #     row_king = 0
        #     col_king = 0
        #     for row in range(1, len(board)):
        #         for col in range(1, len(board[row])):
        #             if board[row][col].color == '♚':
        #                row_king = row
        #                col_king = col
        #                break
        #         if row_king + col_king == 0:
        #             break
        #
        #     for row in range(1, len(board)):
        #         for col in range(1, len(board[row])):
        #             if board[row][col].color in black_characters:
        #                 if board[row][col].check_steps(row, col, row_king, col_king, board):
        #                     return True
        # else:
        #     row_king = 0
        #     col_king = 0
        #     for row in range(1, len(board)):
        #         for col in range(1, len(board[row])):
        #             if board[row][col].color == '♔':
        #                 row_king = row
        #                 col_king = col
        #                 break
        #         if row_king + col_king == 0:
        #             break
        #
        #
        #         for row in range(1, len(board)):
        #             for col in range(1, len(board[row])):
        #                 if board[row][col].color in white_characters:
        #                     if board[row][col].check_steps(row, col, row_king, col_king, board):
        #                         return True
        return False



