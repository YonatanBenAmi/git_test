from classsim import ChessCharacter


class Queen(ChessCharacter):
    def steps(self, row1, row2, col1, col2):
        self.row1 = row1
        self.row2 = row2
        self.col1 = col1
        self.col2 = col2

        return abs(self.row1 - self.row2) == abs(self.col1 - self.col2) \
            or self.row1 == self.row2 or self.col1 == self.col2

    def check_steps(self, num):
        self.num = num
        if self.num > 7 or self.num < 0:
            return False
        return True


def main():
    a = Queen(paint, location, life_status)
    row1 = int(input("Enter row1: "))
    while not a.check_steps(row1):
        row1 = int(input("Enter row1: "))

    col1 = int(input("Enter col1: "))
    while not a.check_steps(col1):
        col1 = int(input("Enter col1: "))

    print('Current player position - (row, column):', (row1, col1))

    row2 = int(input("Enter row2: "))
    while not a.check_steps(row2):
        row2 = int(input("Enter row2: "))

    col2 = int(input("Enter col2: "))
    while not a.check_steps(col2):
        col2 = int(input("Enter col2: "))
    print('Position the player wants to move - (row, column):', (row2, col2))

    print(a.steps(row1, row2, col1, col2))


main()
