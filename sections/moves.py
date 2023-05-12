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
    horse_type:(((2,1),(2,-1),(-2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)),),
    queen_type:((straight_move),(diagonal_move)),
    }
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
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
#queen_b_
#pawn_b__
#king_b__
#tower_b_
#bishop_b
#knight_b
#00000000
#////////
class Game():
    #an attempt to define a chessboard
    def __init__(self,table,):
        self.table=table
        self.move_color=0
    
    def move_a_piece(self):
        #method that tries to move a piece
        if self.move_color==0:
            self.move_color=1
            print("white moved,black to move")
        elif self.move_color==1:
            self.move_color=0
            print("black moved, white to move")
        
            
    

    
class Piece():
    #an attempt to define a chess.piece
    def __init__(self,chess_type,color,position):
        self.chess_type=chess_type
        self.color=color
        self.position=position
        
    def name(self):
        #gives the complete name of a piece
        name=(str(color)+"_"+str(chess_type))
        return name
b_,w_=0,0
pawn__=0
knight=0
bishop=0
king__=0
queen_=0
tower_=0
#creation of istances rapresentative of pieces
p1= Piece(pawn__,b_,(7,a))
p2= Piece(pawn__,b_,(7,b))
p3= Piece(pawn__,b_,(7,c))
p4= Piece(pawn__,b_,(7,d))
p5= Piece(pawn__,b_,(7,e))
p6= Piece(pawn__,b_,(7,f))
p7= Piece(pawn__,b_,(7,g))
p8= Piece(pawn__,b_,(7,h))
p9= Piece(pawn__,w_,(2,a))
p10= Piece(pawn__,w_,(2,b))
p11= Piece(pawn__,w_,(2,c))
p12= Piece(pawn__,w_,(2,d))
p13= Piece(pawn__,w_,(2,e))
p14= Piece(pawn__,w_,(2,f))
p15= Piece(pawn__,w_,(2,g))
p16= Piece(pawn__,w_,(2,h))
p17= Piece(knight,b_,(8,b))
p18= Piece(knight,b_,(8,g))
p19= Piece(knight,w_,(1,b))
p20= Piece(knight,w_,(1,g))
p21= Piece(bishop,b_,(8,c))
p22= Piece(bishop,b_,(8,f))
p23= Piece(bishop,w_,(1,c))
p24= Piece(bishop,w_,(1,f))
p25= Piece(tower_,b_,(8,a))
p26= Piece(tower_,b_,(8,h))
p27= Piece(tower_,w_,(1,a))
p28= Piece(tower_,w_,(1,h))
p29= Piece(queen_,b_,(8,d))
p30= Piece(queen_,w_,(1,d))
p31= Piece(king__,b_,(8,e))
p32= Piece(king__,w_,(1,e))
pieces=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,
        p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32]




        

new_game= Game(chessboard)
new_game.move_a_piece()
new_game.move_a_piece()


    


