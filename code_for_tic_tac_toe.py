board=[" "for i in range(9)]


def making_board():
    print(board[0], " | ", board[1], " | ", board[2])
    print("---------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("---------------")
    print(board[6], " | ", board[7], " | ", board[8])


def checking_winner(user_input):
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

round=1
current_player = "X"
while True:
    user_input = input(f"Please choose a number between 1 and 9 :it is {current_player}'s turn'")

    if not user_input.isnumeric():
        print("Input must be number")

        continue
    user_input = int(user_input)
    if 1 < user_input > 9:
        print("The number must be between 1 and 9")
        continue

    user_input = int(user_input) - 1
    if board[user_input] == " ":
        board[user_input] = current_player
        making_board()
        if checking_winner(current_player):
            print(f"player {current_player} wins")

            keep_play_or_not = input("If you want to play again.Please type r and q for quit").lower()
            if keep_play_or_not == "r":
                round += 1
                print("round", round)

                continue
            elif keep_play_or_not == "q":
                print("Thanks for playing")
                break
        elif ' ' not in board:
            print("It is draw")

            keep_play_or_not = input("If you want to play again.Please type r and q for quit").lower()
            if keep_play_or_not == "r":
                continue
            elif keep_play_or_not == "q":
                print("Thanks for playing")
                break
    else:
        print("The index is already occupied please choose another")
        continue
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"



