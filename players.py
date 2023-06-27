from  chess_bord import Chess_board
class players:
    def __init__(self,map_squrs={},chess_board=Chess_board()):
        self.chess_board = chess_board
        self.map_squrs = map_squrs

    def map_location(self, chess_board=[]):
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
            print("pick from squar")
            a = input()
            if a in self.map_squrs:
                print("pick to squar")
                b = input()
                if b in self.map_squrs:
                    print("wright corrdinations")
                    a = list(self.map_squrs[a])
                    b = list(self.map_squrs[b])
                    print(a,b)
                    self.chess_board[int(b[0])][int(b[1])] = self.chess_board[int(a[0])][int(a[1])]
                    self.chess_board[int(a[0])][int(a[1])] = chr(11055)
                    break
            else:
                print("worng cordination")

    def print_chess_board(self):
        for col in range(0, 9):
            print(*self.chess_board[col])
        print()

#
# a = players()
# a.map_location()
# a.move_chess_board()