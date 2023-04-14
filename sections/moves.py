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

king_moves=((1,1),(1,-1),(-1,1),(-1,-1),
            (1,0),(0,1),(-1,0),(0,-1))
            #dictionary of info about the horse piece
horse_type={
    moves:((2,1),(2,-1),(-2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2))
    }
#dictionary of info about the pawn
pawn_type={
    moves:((0,1),(en_passant),(pawn_capture))
    }
#dictionary of info about the bishop
bishop_type={
    moves:((diagonal_move),)
    }
#dictionary of info about the tower
tower_type={
    moves:((straight_move),)
    }
#dictionary of info about the king
king_type={
    moves:((castle_long),(castle_short),(king_moves))
           }


