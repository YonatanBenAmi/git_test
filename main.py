from chess_bord import Chess_board
from players import Players
game = Chess_board()
game.create_new_board_game_start()
game.print_board()
player1 = Players(game.board)
player1.map_location()
while True:
    player1.move_chess_board()
    player1.print_chess_board()
