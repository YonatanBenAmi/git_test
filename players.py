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
                            if self.king_threat():
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
                                print("your king is in threat")
                                if self.chess_board[a[0]][a[1]].check_steps(a[0], a[1], b[0], b[1], self.chess_board) and self.king_threat() == True:
                                    self.chess_board[int(b[0])][int(b[1])] = self.chess_board[int(a[0])][int(a[1])]
                                    self.chess_board[int(a[0])][int(a[1])] = Tav(chr(11055))
                                    if self.king_threat() == True:
                                        if self.turn == "white":
                                            self.turn = "black"
                                            break
                                        else:
                                            self.turn = "white"
                                            break
                                    else:
                                        print("your king still in threat")
                                        self.chess_board[int(a[0])][int(a[1])] =  self.chess_board[int(b[0])][int(b[1])]
                                        self.chess_board[int(a[0])][int(a[1])] = Tav(chr(11055))
                    else:
                        print("pick your own tools ")


    def print_chess_board(self):
        for col in range(0, 9):
            print(*self.chess_board[col])
        print()

    def king_threat(self):
        flag = False
        for row in range(1,len(self.chess_board)):
            for col in range(1,len(self.chess_board[row])):
                if self.turn == "white":
                    if self.chess_board[row][col].color == '♚':
                        king = self.chess_board[row][col]
                        row1 = row
                        col1 = col
                        flag == True
                        break
                if self.turn == "black":
                    if self.chess_board[row][col].color == '♔':
                        king = self.chess_board[row][col]
                        row1 = row
                        col1 = col
                        flag == True
                        break
            if flag:
                break
        for row in range(1,len(self.chess_board)):
            for col in range(1,len(self.chess_board[row])):
                if self.chess_board[row][col].check_steps(row, col, row1, col1,self.chess_board):
                    return False
        return True


    def is_end_game(self):
        pass
