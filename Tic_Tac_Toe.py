from random import randrange
from copy import deepcopy
from pprint import pprint

# for i in range(10):
#     print(randrange(8))

game_on = True

squares =  {1 : (0, 0), 
            2 : (0, 1), 
            3 : (0, 2), 
            4 : (1, 0), 
            5 : (1, 1),
            6 : (1, 2),
            7 : (2, 0),
            8 : (2, 1),
            9 : (2, 2)} 
""" Possible auto-fill of this dictionary"""

the_board = [[ 0 for col in range(3)] for row in range(3)]


the_board[0][0] = 1
the_board[0][1] = 2
the_board[0][2] = 3
the_board[1][0] = 4
the_board[1][1] = 5
the_board[1][2] = 6
the_board[2][0] = 7
the_board[2][1] = 8
the_board[2][2] = 9  
""" Possible auto-fill of this matrix"""


def display_board(the_board):

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" )
    print("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" )
    print("|" + " " * 2, the_board[0][0], " " * 2 + "|" + " " * 2, the_board[0][1], " " * 2 + "|" + " " * 2, the_board[0][2], " " * 2 + "|")
    print("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" )
    print("+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" )
    print("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" )
    print("|" + " " * 2 , the_board[1][0] ," " * 2 + "|" + " " * 2 ,the_board[1][1] ," " * 2 + "|" + " " * 2 , the_board[1][2] , " " * 2 + "|")
    print("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" )
    print("+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" )
    print("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" )
    print("|" + " " * 2 , the_board[2][0] , " " * 2 + "|" + " " * 2 , the_board[2][1] , " " * 2 + "|" + " " * 2 , the_board[2][2] , " " * 2 + "|")
    print("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|" )
    print("+" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+" )

def make_list_of_free_fields(the_board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []


    for row in range(3):
        for col in range(3):
            
            if the_board[row][col] != "O" and the_board[row][col] != "X":
                free_fields.append((row, col))

            

    return free_fields

def victory_for(the_board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
            
    # Column check

    if the_board[0][0] == sign and the_board[0][1] == sign and the_board[0][2] == sign:

        win_response(sign)
    
    elif the_board[1][0] == sign and the_board[1][1] == sign and the_board[1][2] == sign:

        win_response(sign)
    
    elif the_board[2][0] == sign and the_board[2][1] == sign and the_board[2][2] == sign:

        win_response(sign)

    # Row check

    elif the_board[0][0] == sign and the_board[1][0] == sign and the_board[2][0] == sign:

        win_response(sign)

    elif the_board[0][1] == sign and the_board[1][1] == sign and the_board[2][1] == sign:

        win_response(sign)

    elif the_board[0][2] == sign and the_board[1][2] == sign and the_board[2][2] == sign:

        win_response(sign)

    # Diagonal check

    elif the_board[0][0] == sign and the_board[1][1] == sign and the_board[2][2] == sign:

        win_response(sign)

    elif the_board[0][2] == sign and the_board[1][1] == sign and the_board[2][0] == sign:

        win_response(sign)
            
    elif make_list_of_free_fields(the_board) == []:

        print("Game is tied.")

        replay()

    else:

        return None


def enter_move(the_board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.
    try:
        player_move = int(input("Please enter your move: "))
        make_list_of_free_fields(the_board)
        matched = False

        print(player_move)

        for row in range(3):
            for col in range(3):
                
                if player_move < 1 or player_move > 9:

                    print ("Please select a number within the range 1 - 9.")
                    display_board(the_board)
                    enter_move(the_board)
                    
                    break
        
                elif squares[player_move] not in make_list_of_free_fields(the_board):

                    print("Field not available.")
                    display_board(the_board)
                    enter_move(the_board)
                
                    break
                
                elif player_move == the_board[row][col]:

                    the_board[row][col] = "O"
                    make_list_of_free_fields(the_board)
                    matched = True
                    # draw_move(the_board)
                    break

            if matched:
                break

    except ValueError:
        print ("Please select an integer.")
        enter_move(the_board)


    
    


def replay():
    # Gives the player an option to replay the game.

    global game_on

    game_on_check = input("Try again? ")

    if game_on_check in ("Yes", "y", "yes", "Y"):

         
        game_on = True

        the_board[0][0] = 1
        the_board[0][1] = 2
        the_board[0][2] = 3
        the_board[1][0] = 4
        the_board[1][1] = 5
        the_board[1][2] = 6
        the_board[2][0] = 7
        the_board[2][1] = 8
        the_board[2][2] = 9

    elif game_on_check in ("No","N","no"):

        print("Cheers!")

        game_on = False

    else: 

        game_on_check = input("Yes or No? ")

        if game_on_check in ("No","N","no"):

            game_on = False
            
        else:

            game_on = False


     

def win_response(sign):

    display_board(the_board)
  

    if sign == "X":

        print("Computer Wins. That's the end!")

    else:
        print("Player Wins!")

    replay()
       

    

def draw_move(the_board):
    # The function draws the computer's move and updates the board.

    elem1 = randrange(1,10)
                

    if the_board[1][1] != "X":

        print("Time to play Tic Tac Toe. The Computer moves first: ")
        print("The computer moved to square", the_board[1][1])


        the_board[1][1] = "X"


    elif squares[elem1] in make_list_of_free_fields(the_board):

        the_board[squares[elem1][0]][squares[elem1][1]] = "X"

        print("The computer moved to square" , elem1, "Your move.")

    else:

        draw_move(the_board)
    


while game_on:

    draw_move(the_board)

    

    victory_for(the_board, "X")

    display_board(the_board)

    if game_on == False:
        break

    enter_move(the_board)


    victory_for(the_board, "O")

    display_board(the_board)

    if game_on == False:
        break



