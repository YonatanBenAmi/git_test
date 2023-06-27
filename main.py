from chess_bord import Chess_board
from pawn import Pawn
from players import Players
from classsim import ChessCharacter
from point import Point
game = Chess_board()
# game.create_new_board_game_start()
game.create_new_board()
game.fill_in_all_chrecters()
game.print_board()
player1 = Players([], game.board)
player1.map_location()
while True:
    player1.move_chess_board()
    player1.print_chess_board()

