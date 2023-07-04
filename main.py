from chess_bord import Chess_board
from players import Players

game = Chess_board()
game.create_new_board_game_start()
game.print_board()
players = Players(game.board)
players.map_location()
while True:
    players.move_chess_board()
    players.print_chess_board()
    if players.is_end_game():
        print("end game")
        break

