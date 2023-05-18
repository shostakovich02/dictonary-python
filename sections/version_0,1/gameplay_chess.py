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
    move_color=0
    while not checkmate:
        if move_color==0:
        
            move_a_piece(cb.chessboard,cb.pieces,move_color)
            cb.nice_print(cb.chessboard,cb.pieces)
            
            move_color=1
            print("white moved,black to move")
        elif move_color==1:
            move_a_piece(cb.chessboard,cb.pieces,move_color)
            cb.nice_print(cb.chessboard,cb.pieces)
        
            move_color=0
            print("black moved, white to move")
    print("the match ended")
def movable_pieces(pieces,move_color):
    #function that determines movable pieces
    #here you should add dead/alive quality
    alive_and_dead_movables=[]
    white_alive=[]
    black_alive=[]
    movables=[]
    
    for b in black_pieces:
        if b.alive:
            black_alive.append(b)
    for w in white_pieces:
        if w.alive:
            white_alive.append(w)
    all_alive_pieces=white_alive+black_alive      
        
        
    if move_color==0:
        movables=white_alive,black_alive,all_alive_pieces
    else:
        movables=black_alive,white_alive,all_alive_pieces
    
        
    
    return movables

def line_of_fire(moving_piece,move):
    #this function returns a list of coordinates of spots in the line of fire of a long range piece
    
    spots=[]
    diagonal_long_moves=[
                        (2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(-2,-2),(-3,3),(-4,-4),(-5,5),(-6,-6),(-7,-7),
                        (-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7)
                        ]
    lateral_long_moves=[
                        (2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                        (-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7)
                        ]
    
    
        
    if move in lateral_long_moves:
        #considering possible cases of rook_like movements
        if move[0]==0:
            #case in which the movement is vertical, subcases considering if its an advance or a retreat
            
            if move[1]>0:
                for i in range(0,(move[1])):
                    spots.append(moving_piece.pos_pos((0,i)))
            
                
            else:
                for i in range((move[1]),0):
                    spots.append(moving_piece.pos_pos((0,i)))
                
            
        else:
            #case in which the movement is horizontal, subcases considering whether the movement is to the left or to the right
            if move[0]>0:
                for i in range (0,(move[0])):
                    spots.append(moving_piece.pos_pos((i,0)))
                    
            else:
                for i in range((move[1]),0):
                    spots.append(moving_piece.pos_pos((i,0)))
    elif move in diagonal_long_moves:
        #considering possible cases of bishop_like movements
        
        
        if move[0]>0:
            #considering moves depending on negativity and positivity of axis_related movements
            if move[1]>0:
                for i in range (0,move[0]):
                    spots.append(moving_piece.pos_pos((i,i)))
            else:
                for i in range (0,move[0]):
                    spots.append(moving_piece.pos_pos((i,-i)))
        else:
            if move[1]>0:
                for i in range (0,move[1]):
                    spots.append(moving_piece.pos_pos((-i,i)))
            else:
                for i in range (move[0],0):
                    spots.append(moving_piece.pos_pos((i,i)))
            
                
            
        
    else:
        spots=[]
    return spots
    
    
    
    
def move_is_possible(moving_piece,move,chessboard,pieces):
    #function that determines whether a certain move of a certain piece on a certain chessboard is possible
    
    impossibility_type=""
    if type(move) == str:
        #this if conditionseparets complex situation likke castling from more generic moves like diagonal
        a=False
    
    else:
        #imposing the "out of the board condition"
        out_condition_x=(1>(moving_piece.position[0]+move[0]))or((moving_piece.position[0]+move[0])>8)
        out_condition_y=(1>(moving_piece.position[1]+move[1]))or((moving_piece.position[0]+move[0])>8)
        
        if out_condition_x or out_condition_y:
            a=False
            impossibility_type="out"
        else:
            #prerequisites to "friendly fire condition"
            num=0
            possible_position=moving_piece.pos_pos(move)
            movables=(movable_pieces(pieces,move_color))[0]
            for _piece_ in movables:
                if possible_position== _piece_.position:
                    num=num+1
            #friendly fire condition
            if num!=0:
                a=False
                impossibility_type="friendly_fire"
                
            else:
                #prerequisites of "line of fire condition"
                line_of_sight=[]
                line_of_sight=line_of_fire(moving_piece,move)
                all_alive=(movable_pieces(pieces,move_color))[2]
                counter=0
                
                for spot in line_of_sight:
                    for obstruction in all_alive:
                        coordinates= obstruction.position
                        
                        if (spot[0]==coordinates[0])and(spot[1]==coordinates[1]):
                            counter=counter+1
                    
                    
                if counter!=0:
                    a=False
                    impossibility_type="line_of_fire"
                    
                else:
                    
                
                    a=True
    
       
    return ((a),(impossibility_type))

def possible_moves(chessboard,pieces,move_color):
    #function that expresses the possible move a player can do in the turn
    #first step is to discover what pieces can move and constuct a list of those
    movables=(movable_pieces(cb.pieces,move_color))[0]
    
    
    possible_moves=[]
    out_impossibilities=[]
    friendly_fire_impossibilities=[]
    line_of_fire_impossibilities=[]
    type4_impossibilities=[]
    for _piece_ in movables:
        moves_per_pieces=_piece_.move_type()
        for move in moves_per_pieces:
            composed_move="too complex of a move for now"
            
            #if clause to be certain string_like moves,castles for example, do not get in the way of the list-making process
            if type(move) is not str:
                
                composed_move=((_piece_.position),(_piece_.name()),(_piece_.pos_pos(move)))
            if (move_is_possible(_piece_,move,chessboard,pieces))[0]:
                possible_moves.append(composed_move)
                
            elif (move_is_possible(_piece_,move,chessboard,pieces))[1] == "out": 
                out_impossibilities.append(composed_move)
                
            elif (move_is_possible(_piece_,move,chessboard,pieces))[1] =="friendly_fire":
                friendly_fire_impossibilities.append(composed_move)
                
            elif (move_is_possible(_piece_,move,chessboard,pieces))[1] =="line_of_fire":
                line_of_fire_impossibilities.append(composed_move)
            
        
    return possible_moves,out_impossibilities,friendly_fire_impossibilities,line_of_fire_impossibilities
#the function superior to this comment should also releasr impossibilities
def move_transformer(msg):
    L=[]
    #here cases of special moves are expressed
    if  type(msg) is not str:
        
        return "error"
    elif len(msg) !=5:
        
        return "error"
    else:
        possible_letters=["a","b","c","d","e","f","g","h"]
        possible_numbers=["1","2","3","4","5","6","7","8"]
        type_of_charachter_in_string=(msg[0] in possible_letters) and \
                                      (msg[3] in possible_letters) and \
                                      (msg[1] in possible_numbers) and \
                                      (msg[4] in possible_numbers)
        if not type_of_charachter_in_string:
            
            return"error"
        else:
            for c in msg:
                
                if c in possible_letters:
                    L.append(possible_letters.index(c)+1)
                    
                elif c in possible_numbers:
                    L.append(possible_numbers.index(c)+1)
    return L
                    
                
            
            
            

def move_a_piece(chessboard,pieces,move_color):
    #function that moves a piece through the chessboard
    msg=input("request help with possible moves using help, or insert your move using the  format e2,e4 : ")
    moves_that_are_possible=((possible_moves(cb.chessboard,cb.pieces,move_color))[0])
    if msg is not "help":
        
        requested_move=move_transformer(msg)
        if requested_move == "error":
            print("error in writing the move correctly")
            move_a_piece(cb.chessboard,cb.pieces,move_color)
        
        moves_that_are_possible=((possible_moves(cb.chessboard,cb.pieces,move_color))[0])
        out_of_the_chessboard=((possible_moves(cb.chessboard,cb.pieces,move_color))[1])
        friendly_fire_moves=((possible_moves(cb.chessboard,cb.pieces,move_color))[2])
        line_of_fire_moves=((possible_moves(cb.chessboard,cb.pieces,move_color))[3])
        
        requested_starting_position=((requested_move[0]),(requested_move[1]),)
        
        req_moving_piece=0
        for p in pieces:
            if p.position== requested_starting_position:
                req_moving_piece=p
        if req_moving_piece==0:
            print("move not inserted in the correct format")
            move_a_piece(cb.chessboard,cb.pieces,move_color)
            
        
            
        requested_new_move=(requested_move[2],requested_move[3])
        complete_name_requested=((req_moving_piece.position),(req_moving_piece.name()),(requested_new_move))
        #print(complete_name_requested)
        #print(moves_that_are_possible)
                
        
        
            
            
            
        if complete_name_requested in moves_that_are_possible:
            req_moving_piece.position=requested_new_move
            return "move is possible"
            
            
        else:
            
            if complete_name_requested in out_of_the_chessboard:
                print("move is not possible,out of the chessboard")
            elif complete_name_requested in friendly_fire_moves:
                print("move is not possible,friendly_fire")
            elif line_of_fire_moves in line_of_fire_moves:
                print("move is not possible,line of fire ignored")
            else:
                print("something went wrong")
            move_a_piece(cb.chessboard,cb.pieces,move_color)
    elif msg is "help":
            
        print(moves_that_are_possible)
        move_a_piece(cb.chessboard,cb.pieces,move_color)                
                
#((5, 2), 'w_pawn__', (5, 3))           
#((5, 2), 'w_pawn__', (5, 3))  
make_a_move(cb.chessboard,cb.pieces)   
        #return moves_that_are_possible,out_of_the_chessboard,friendly_fire_moves,line_of_fire_moves
#print(move_a_piece(cb.chessboard,cb.pieces,0)[0])
#print((move_a_piece(cb.chessboard,cb.pieces,0)[1]))
#print((move_a_piece(cb.chessboard,cb.pieces,0)[2]))
#print((move_a_piece(cb.chessboard,cb.pieces,0)[3]))
#for i in (movable_pieces(cb.pieces,move_color))[0]:
 #   print(i.position)
  #  print(i.name())
    
#prossimi step
    #risolto:instaurare legame tra mossa inserita e compatibilità con mosse possibili
    #effetto pezzo mangiato
    #condizione di scacco
    #condizione di auto_scacco
    
