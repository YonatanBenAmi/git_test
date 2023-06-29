from chess_bord import Chess_board
from tav import Tav
from rook import Rook


class Players:
    def __init__(self,chess_board=Chess_board(), turn="white", map_squrs={}):
        self.chess_board = chess_board
        self.map_squrs = map_squrs
        self.turn = turn

    def map_location(self):
        self.map_squrs = {}
        leter = "a"
        for row in range(1, 9):
            for col in range(1, 9):
                self.map_squrs[leter+str(col)] = (row, col)
            leter = ord(leter)

            leter += 1
            leter = chr(leter)

    def move_chess_board(self):
        while True:
            a = input("pick from square or for castling press 1 ")
            if a != '1':
                if a in self.map_squrs:
                    b = input("pick to square ")
                    if b in self.map_squrs:
                        # print("wright corrdinations \n")
                        a = list(self.map_squrs[a])
                        b = list(self.map_squrs[b])
                        black_characters = ['♙', '♘', '♗', '♖', '♕', '♔']
                        white_characters = ['♟', '♞', '♝', '♜', '♛', '♚']
                        if (self.turn == "white" and self.chess_board[a[0]][a[1]].color in white_characters)\
                            or (self.turn == "black" and self.chess_board[a[0]][a[1]].color in black_characters):
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
                                print('1worng cordinatins')
                        else:
                            print("2worng cordination")
                    else:
                        print("3worng cordination")
                else:
                    print("4worng cordination")
            else:
                castling()

    def print_chess_board(self):
        for col in range(0, 9):
            print(*self.chess_board[col])
        print()


# a = Players()
# a.map_location()
# print(a.map_squrs)
# a.move_chess_board()

# and self.chess_board[a[0]][a[1]] in white_characters)
# and self.chess_board[a[0]][a[1]] in black_characters
