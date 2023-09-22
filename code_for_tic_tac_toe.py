# Title-Tic Tac Toe
## Member_names
### Min Myat Ngwe
### Juyin Tang
### Duc Minh Khang Nguyen
### Nguyen Ngoc  Tu Anh
import random 
board = [" " for i in range(9)] #making board
def making_board():
    print(board[0],  " | " ,board[1],  " | " ,board[2])
    print("---------------")
    print(board[3],  " | " ,board[4],  " | " ,board[5])
    print("---------------")
    print(board[6],  " | " ,board[7],  " | " ,board[8])
    

def checking_winner(user_input): #checking who is winner
    if user_input == board[0] and user_input == board[1] and user_input == board[2]:
        return True
    if user_input == board[0] and user_input == board[3] and user_input == board[6]:
        return True
    if user_input == board[1] and user_input == board[4] and user_input == board[7]:
        return True
    if user_input == board[2] and user_input == board[5] and user_input == board[8]:
        return True
    if user_input == board[3] and user_input == board[4] and user_input == board[5]:
        return True
    if user_input == board[6] and user_input == board[7] and user_input == board[8]:
        return True
    if user_input == board[0] and user_input == board[4] and user_input == board[8]:
        return True
    if user_input == board[2] and user_input == board[4] and user_input == board[5]:
        return True
    def restart_quit(user_input): # restart or quit
    if user_input == "r":
        return True
    elif user_input == "q":
        return False

round = 1 # to know the round 
current_player =["X","O"]
current_player=random.choice(current_player)
while True:
    user_input = input(f"Please choose a number between 1 and 9: it is {current_player}'s turn")

    if not user_input.isnumeric(): #only number is accepted
        print("Input must be a number")
        continue

    user_input = int(user_input)

    if user_input < 1 or user_input > 9:  #the number must be between 1 and 9
        print("The number must be between 1 and 9")
        continue

    user_input -= 1   #subtract 1 to get real index
    if board[user_input] == " ": # checking if there any " "
        board[user_input] = current_player
        making_board()
        if checking_winner(current_player):
            print(f"Player {current_player} wins")  #printing th winner

            keep_play_or_not = input("If you want to play again, please type 'r' or 'q' to quit: ").lower()
            if restart_quit(keep_play_or_not):
                round += 1
                print("Round", round)
                board = [" " for i in range(9)] #restarting the board
                current_player = "X"
                continue
            else:
                print("Thanks for playing")#quitting the game
                break

        elif ' ' not in board:#if there is no " " to insert it is considered draw
            print("It's a draw")

            keep_play_or_not = input("If you want to play again, please type 'r' or 'q' to quit: ").lower()
            if restart_quit(keep_play_or_not):
                round += 1
                print("Round", round)
                board = [" " for i in range(9)]
                current_player = "X"
                continue
            else:
                print("Thanks for playing")
                break
    else:
        print("The index is already occupied. Please choose another.")
        continue

    if current_player == "X":# changing the player
        current_player = "O"
    else:
        current_player = "X"
# conclusion
The goal of this qroject is to remember the thing that we were used to playing when we were kids.And. it is interesting to make with python.
## finalise
- This programm is designned to only accept the number which are between 1 and 9.If words or the number which is greater than 9 or small than 1 is inserted.The programm will print  "The number must be between 1 and 9" and continue the loop until the user input the right thing.
- This is programmed to ask whether the user wants to play again or not.After each match,the user will be asked if he want to play another round or not.If he wants to play just need to input r and q for quit.
- To have a fair match the first move is randomly choosed by using random libries.


