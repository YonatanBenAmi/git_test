from point import Point


class ChessCharacter:
    def __init__(self, color="", point=None):
        if point is None:
            self.point = Point()
        else:
            self.point = point
        self.color = color

    # def check_steps(self):
    #         if (self.point.row < 9 or self.point.row > 0) and (self.point.col < 9 or self.point.col > 0):
    #                 return True
    #         return False
    #

    # def get_point(self):
    #         return self.point
