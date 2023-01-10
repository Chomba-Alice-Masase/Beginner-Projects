# Second prototype of our tictactoe game
# we will try and implement it a bit better
import random
game_board = (
            'A', 'B', 'C',
            'D', 'E', 'F',  # Our game board
            'G', 'H', 'I'
             )
Available_Moves = [
            'A', 'B', 'C',
            'D', 'E', 'F',  # Our list of available moves
            'G', 'H', 'I'
        ]
Winning_Moves = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],  # move sets that indicate a win
    ['A', 'D', 'G'],
    ['B', 'E', 'H'],
    ['C', 'F', 'I'],
    ['A', 'E', 'I'],
    ['G', 'E', 'C']
]
Player_Moves = []  # stores moves made by the player
Python_Moves = []  # stores moves made by Python
Player_Count = 0 # used later in the code
Python_Count = 0 # //
Game_Active = False
Activate_Game = input("Would you like to face Python in a game of tictactoe? Yes/No: ")  # prompt to activate game
if Activate_Game == "Yes":
    Game_Active = True
    while Game_Active:
        Player_Move = input("Your move: ")  # use the indices instead of the actual coordinates
        if Player_Move in Available_Moves:
            print("You played " + Player_Move)
            Player_Moves.append(Player_Move)
            Available_Moves.remove(Player_Move)
            if 'A' in Player_Moves and 'B' in Player_Moves and 'C' in Player_Moves:
                print("You win!")
                print("Winning move is A B C")
                break
            elif 'D' in Player_Moves and 'E' in Player_Moves and 'F' in Player_Moves:
                print("You win!")
                print("Winning move is D E F")
                break
            elif 'G' in Player_Moves and 'H' in Player_Moves and 'I' in Player_Moves:
                print("You win!")
                print("Winning move is G H I")
                break
            elif 'A' in Player_Moves and 'D' in Player_Moves and 'G' in Player_Moves:
                print("You win!")
                print("Winning move is A B C")
                break
            elif 'E' in Player_Moves and 'B' in Player_Moves and 'H' in Player_Moves:
                print("You win!")
                print("Winning move is E B H")
                break
            elif 'C' in Player_Moves and 'F' in Player_Moves and 'I' in Player_Moves:
                print("You win!")
                print("Winning move is C F I")
                break
            elif 'A' in Player_Moves and 'E' in Player_Moves and 'I' in Player_Moves:
                print("You win!")
                print("Winning move is A E I")
                break
            elif 'G' in Player_Moves and 'E' in Player_Moves and 'C' in Player_Moves:
                print("You win!")
                print("Winning move is G E C")
                break
           # print("Remaining moves: ")
            #print(Available_Moves)
        else:
            print("Already Played")
            continue
        if len(Available_Moves)==0:
            print("Draw")
            Game_Active = False

        else:
            Python_Move = random.choice(Available_Moves)
            print("Python played " + Python_Move)
            Python_Moves.append(Python_Move)
            Available_Moves.remove(Python_Move)

            if 'A' in Python_Moves and 'B' in Python_Moves and 'C' in Python_Moves:
                print("Python wins!")
                print("Winning move is A B C")
                break
            elif 'D' in Python_Moves and 'E' in Python_Moves and 'F' in Python_Moves:
                print("Python wins!")
                print("Winning move is D E F")
                break
            elif 'G' in Python_Moves and 'H' in Python_Moves and 'I' in Python_Moves:
                print("Python wins!")
                print("Winning move is G H I")
                break
            elif 'A' in Python_Moves and 'D' in Python_Moves and 'G' in Python_Moves:
                print("Python wins!")
                print("Winning move is A D G")
                break
            elif 'B' in Python_Moves and 'E' in Python_Moves and 'H' in Python_Moves:
                print("Python wins!")
                print("Winning move is B E H")
                break
            elif 'C' in Python_Moves and 'F' in Python_Moves and 'I' in Python_Moves:
                print("Python wins!")
                print("Winning move is C F I")
                break
            elif 'A' in Python_Moves and 'E' in Python_Moves and 'I' in Python_Moves:
                print("Python wins!")
                print("Winning move is A E I")
                break
            elif 'G' in Python_Moves and 'E' in Python_Moves and 'C' in Python_Moves:
                print("Python wins!")
                print("Winning move is G E C")
                break
            print("Remaining moves: ")
            print(Available_Moves)


        #Now we create a way for the game to be won
        #using the long method...


        #  Commented code is unused code that didn't work
       



else:
 print("Bye!")
 quit()
