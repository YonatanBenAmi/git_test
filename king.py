from classsim import ChessCharacter
from point import Point
class King(ChessCharacter):
    def __init__(self,color="", point=Point(),status_move=False):
        super().__init__(color, point)
        self._status_move = status_move

    def __str__(self):
        return self.color

    def check_steps(self, row1, col1, row2, col2):
        return abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1

    def check_two_places_same_group(self, row1, col1, row2, col2):
        pass



























#     def check_steps(self, num):
#         self.num = num
#         if self.num > 7 or self.num < 0:
#             return False
#         return True
#
#     def steps(self, row1, row2, col1, col2):
#         self.row1 = row1
#         self.row2 = row2
#         self.col1 = col1
#         self.col2 = col2
#
#         return abs(self.row1 - self.row2) <= 1 and abs(self.col1 - self.col2) <= 1
#
#     def castling(self):
#         pass
#
#
# def main():
#     a = King()
#     row1 = int(input("Enter row1: "))
#     while not a.check_steps(row1):
#         row1 = int(input("Enter row1: "))
#
#     col1 = int(input("Enter col1: "))
#     while not a.check_steps(col1):
#         col1 = int(input("Enter col1: "))
#
#     print('Current player position - (row, column):', (row1, col1))
#
#     row2 = int(input("Enter row2: "))
#     while not a.check_steps(row2):
#         row2 = int(input("Enter row2: "))
#
#     col2 = int(input("Enter col2: "))
#     while not a.check_steps(col2):
#         col2 = int(input("Enter col2: "))
#     print('Position the player wants to move - (row, column):', (row2, col2))
#
#     print('The player has entered a possible location: ', a.steps(row1, row2, col1, col2))
#
#
# main()
