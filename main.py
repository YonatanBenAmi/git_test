king_black, king_white = chr(0x2654), chr(0x265A)
queen_black, queen_white = chr(0x2655), chr(0x265B)
rook_black, rook_white = chr(0x2656), chr(0x265C)
knight_black, knight_white = chr(0x2658), chr(0x265E)
pawn_black, pawn_white = chr(0x2659), chr(0x265F)
bishop_black, bishop_white = chr(0x2657), chr(0x265D)

array = [[rook_black, knight_black, bishop_black, queen_black, king_black, bishop_black, knight_black, rook_black],
          [pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black],
          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          [pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white],
          [rook_white, knight_white, bishop_white, queen_white, king_white, bishop_white, knight_white, rook_white]]

for i in array:
    print(*i)


