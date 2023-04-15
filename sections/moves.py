moves="moves"
pawn_capture="place_holder"
en_passant="place_holder"
castle_long="place_holder"
castle_short="place_holder"
tower_type="place_holder"
king_type="place_holder"
bishop_type="place_holder"
pawn_type="place_holder"
horse_type="place_holder"
queen_type="place_holder"
#subdefinitions of moves
straight_move=((1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
               (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
               (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),
               (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7))
               
diagonal_move=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),
              (-1,-1),(-2,-2),(-3,3),(-4,-4),(-5,5),(-6,-6),(-7,-7),
              (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),
              (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7))
king_moves=((1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1))

#dictionary of info about the chess pieces
moves:{
    king_type:((castle_long),(castle_short),(king_moves)),
    tower_type:((straight_move),),
    bishop_type:((diagonal_move),),
    pawn_type:((0,1),(en_passant),(pawn_capture)),
    horse_type:((2,1),(2,-1),(-2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)),
    queen_type:((straight_move),(diagonal_move)),
    }
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#building of the chessboard

#playng board definition
chessboard=[[[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            ]
    
#example of empty chessboard 
chessboard_empty=[
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            ]

#simple function the returns ,given a x,y coordinates, the elment present on the relative position on the chessboard
a,b,c,d,e,f,g,h=1,2,3,4,5,6,7,8
def position(x,y):
    return (chessboard[y-1])[x-1]

print (position(1,b))

#definition of on piece
piece_w_1=


    


