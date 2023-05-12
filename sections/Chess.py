#import everything
import chessboard
def open_menu():
    print("welcome to giovanni's chess try, you,r welcome to choose between various options,writing in the console")
    print("due to early stage of developement,the option is limited to one: start!")
    x=input("if you want to start a new game write start in the console : ")
    if x == "start":
        chessboard.start_a_game()

open_menu()


