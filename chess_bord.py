# array = [[rook_black, knight_black, bishop_black, queen_black, king_black, bishop_black, knight_black, rook_black],
#          [pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black],
#          [pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white],
#          [rook_white, knight_white, bishop_white, queen_white, king_white, bishop_white, knight_white,rook_white]]


from colorama import Back, Style, Fore


def create_chess_board():
    chess_board = []
    tav = chr(11055)
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                chess_board.append(Back.WHITE + "  " + Fore.WHITE + str(tav) + "  ")
            else:
                chess_board.append(Back.BLACK + "  " + Fore.BLACK + str(tav) + "  ")
        chess_board.append(Back.RESET)
        chess_board.append("\n")
    return chess_board


def print_board(chess_board):
    print(''.join(chess_board))


def add_pisces_start(chess_board):
    dark_brown = Fore.LIGHTYELLOW_EX
    dark_brown_r = Fore.RED

    king_black = chr(0x2654)
    king_white = chr(0x265A)
    queen_black, queen_white = chr(0x2655), chr(0x265B)
    rook_black, rook_white = chr(0x2656), chr(0x265C)
    knight_black, knight_white = chr(0x2658), chr(0x265E)
    pawn_black, pawn_white = chr(0x2659), chr(0x265F)
    bishop_black, bishop_white = chr(0x2657), chr(0x265D)
    # WHITE ARMY
    chess_board[0] = Back.WHITE + '  ' + dark_brown + rook_black +  "  "
    chess_board[1] = Back.BLACK + '  ' + knight_black + "  "
    chess_board[2] = Back.WHITE + '  ' + bishop_black + "  "
    chess_board[3] = Back.BLACK + '  ' + queen_black + "  "
    chess_board[4] = Back.WHITE + '  ' + king_black + "  "
    chess_board[5] = Back.BLACK + '  ' + bishop_black + "  "
    chess_board[6] = Back.WHITE + '  ' + knight_black + "  "
    chess_board[7] = Back.BLACK + '  ' + rook_black + "  "
    chess_board[10] = Back.BLACK + '  ' + pawn_black + "  "
    chess_board[11] = Back.WHITE + '  ' + pawn_black + "  "
    chess_board[12] = Back.BLACK + '  ' + pawn_black + "  "
    chess_board[13] = Back.WHITE + '  ' + pawn_black + "  "
    chess_board[14] = Back.BLACK + '  ' + pawn_black + "  "
    chess_board[15] = Back.WHITE + '  ' + pawn_black + "  "
    chess_board[16] = Back.BLACK + '  ' + pawn_black + "  "
    chess_board[17] = Back.WHITE + '  ' + pawn_black + "  "
    #BLACK ARMY
    chess_board[-3] = Back.WHITE + '  ' + rook_white + "  "
    chess_board[-4] = Back.BLACK + '  ' + bishop_white + "  "
    chess_board[-5] = Back.WHITE + '  ' + knight_white + "  "
    chess_board[-6] = Back.BLACK + '  ' + king_white + "  "
    chess_board[-7] = Back.WHITE + '  ' + queen_white + "  "
    chess_board[-8] = Back.BLACK + '  ' + knight_white + "  "
    chess_board[-9] = Back.WHITE + '  ' + bishop_white + "  "
    chess_board[-10] = Back.BLACK + '  ' + rook_white + "  "
    chess_board[-13] = Back.BLACK + '  ' + pawn_white + "  "
    chess_board[-14] = Back.WHITE + '  ' + pawn_white + "  "
    chess_board[-15] = Back.BLACK + '  ' + pawn_white + "  "
    chess_board[-16] = Back.WHITE + '  ' + pawn_white + "  "
    chess_board[-17] = Back.BLACK + '  ' + pawn_white + "  "
    chess_board[-18] = Back.WHITE + '  ' + pawn_white + "  "
    chess_board[-19] = Back.BLACK + '  ' + pawn_white + "  "
    chess_board[-20] = Back.WHITE + '  ' + dark_brown_r + pawn_white + "  "

    return chess_board


a = create_chess_board()
a = add_pisces_start(a)
print_board(a)

