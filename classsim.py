

from point import point


class ChessCharacter:
        def __init__(self, color, point=point()):
                self.point = point
                self.color = color

        def get_point(self):
                return self.point



        def check_steps(self):
                if (self.point.row < 9 or self.point.row > 0) and (self.point.col < 9 or self.point.col > 0):
                        return True
                return False




