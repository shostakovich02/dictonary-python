import chessboard as cb
#remember to add dead/alive attribute to piece
    
king_in_Check=False
other_condition=False
checkmate=False
move_color=0   
black_pieces=[]
white_pieces=[]
for _piece_ in cb.pieces:
    if _piece_.color is cb.b_:
        black_pieces.append(_piece_)
    else:
        white_pieces.append(_piece_)


def make_a_move(chessboard,pieces):
    #functions theat helps  the alternation of moves between black and white

    while not checkmate: 
        if move_color==0:
        
            move_a_piece(cb.chessboard,cb.pieces,move_color)
            
            move_color=1
            print("white moved,black to move")
        elif move_color==1:
            move_a_piece(cb.chessboard,cb.pieces,move_color)
        
            move_color=0
            print("black moved, white to move")
    print("the match ended")
def movable_pieces(pieces,move_color):
    #function that determines movable pieces
    #here you should add dead/alive quality
    movables=[]
    if move_color==0:
        movables=white_pieces,black_pieces
    else:
        movables=black_pieces,white_pieces
        
    return movables

def move_is_possible(moving_piece,move,chessboard,pieces):
    #function that determines whether a certain move of a certain piece on a certain chessboard is possible
    
    impossibility_type=""
    if type(move) == str:
        #this if conditionseparets complex situation likke castling from more generic moves like diagonal
        a=False
    
    else:
        #out_condition
        out_condition_x=1>(moving_piece.position[0]+move[0])>8
        out_condition_y=1>(moving_piece.position[1]+move[1])>8
        if out_condition_x or out_condition_y:
            a=False
            impossibility_type="out"
        else:
            a=True
    
       
    return ((a),(impossibility_type))

def possible_moves(chessboard,pieces,move_color):
    #function that expresses the possible move a player can do in the turn
    movables=(movable_pieces(cb.pieces,move_color))[0]
    possible_moves=[]
    out_impossibilities=[]
    type2_impossibilities=[]
    type3_impossibilities=[]
    type4_impossibilities=[]
    for _piece_ in movables:
        moves_per_pieces=_piece_.move_type()
        for move in moves_per_pieces:
            if (move_is_possible(_piece_,move,chessboard,pieces))[0]:
                possible_moves.append(move)
            elif (move_is_possible(_piece_,move,chessboard,pieces))[1] == "out":
                out_impossibilities.append(move)
            
        
    return possible_moves,out_impossibilities
#the function superior to this comment should also releasr impossibilities



def move_a_piece(chessboard,pieces,move_color):
    #function that moves a piece through the chessboard
    msg=input("request help with possible moves using help, or insert your move using the  format e2,e4 : ")
    if msg is "help":
        print("not implemented yet")
        move_a_piece(cb.chessboard,cb.pieces,cb.move_color)
    else:
        requested_move=msg
        moves_that_are_possible=((possible_moves(cb.chessboard,cb.pieces,0))[0])
        out_of_the_chessboard=((possible_moves(cb.chessboard,cb.pieces,0))[1])
        return moves_that_are_possible,out_of_the_chessboard
        
print(move_a_piece(cb.chessboard,cb.pieces,0)[0])

print((move_a_piece(cb.chessboard,cb.pieces,0)[1]))
    
