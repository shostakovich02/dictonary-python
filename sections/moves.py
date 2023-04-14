moves="moves"
pawn_capture="place_holder"
en_passant="place_holder"
castle_long="place_holder"
castle_short="place_holder"

#subdefinitions of moves
straight_move=((1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
               (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
               (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),
               (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7))
               
diagonal_move=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),
              (-1,-1),(-2,-2),(-3,3),(-4,-4),(-5,5),(-6,-6),(-7,-7),
              (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),
              (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7))


#dictionary of info about the chess pieces
moves:{
    king_type:((castle_long),(castle_short),(king_moves))
    tower_type:((straight_move),)
    bishop_type:((diagonal_move),)
    pawn_type:((0,1),(en_passant),(pawn_capture))
    horse_type:((2,1),(2,-1),(-2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2))
    queen_type:((straight_move),(diagonal_move))
    }


