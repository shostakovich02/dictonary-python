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
        
        
    def name(self,):
        #gives the complete name of a piece
        name=(str(self.color)+str(self.chess_type))
        return name

#dummies
b_,w_="b_","w_"
pawn__="pawn__"
knight="knight"
bishop="bishop"
king__="king__"
queen_="queen_"
tower_="tower_"
#definition of letters as rows considering position is respected
a,b,c,d,e,f,g,h=1,2,3,4,5,6,7,8
#function that return the the list corresponding to coordinates
def position_board(x,y,chessboard):
    return (chessboard[(9-y)-1])[(9-x)-1]

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
#creation of list rapresentative of pieces for comfy use in iterations
pieces=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,
        p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32]
#setting up a chessboard for the new game
chessboard=[[[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[]],
            ]
#function that prints nicely adding black and white spaces to the chessboard
def nice_print(chessboard,pieces):
    chessboard=[[[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                ]    
    for _piece_ in pieces:
        y,x=_piece_.position
        position_board(x,y,chessboard).append(_piece_.name())
    
    
    for x in range(1,9):
        for y in range(1,9):
            if position_board(x,y,chessboard)==[]:
                if (x+y)%2==0:
                    #if the sum of indexes is divisible by 2 it is a darksquare
                    position_board(x,y,chessboard).append("////////")
                else:
                    position_board(x,y,chessboard).append("00000000")
    for i in range (0,8):
        print(chessboard[i])
def start_a_game():
    #setting up a new game
    #first step is creating istances rapresenting pieces
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
    

    #setting up a chessboard for the new game
    chessboard=[[[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                ]
    
    
    nice_print(chessboard,pieces)






