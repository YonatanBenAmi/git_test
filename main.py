from pawn import Pawn
from chess_bord import ChessBoard
game = ChessBoard()
game.create_new_board()
a = game.get_board()
pawn = Pawn(2, 2, chr(0x265F))
pawn.check_mov(3, 3, 5, 4, game.get_board())




