import logic2048 as logic

if __name__ == "__main__":
    board = logic.start_game()

while True:
    # get current game state
    status = logic.get_current_state(board)

    # if user lost, end game
    if status == "LOSS":
        print("\n\tYou Lose!\n")
        break
    # if user won, end game
    elif status == "WIN":
        print("\n\tYou Win!\n")
        break

    command = input("\nMove: ")

    # up move for "w" input
    if command.lower() == "w":
        board, flag = logic.move_up(board)
        if status == "CONTINUE" and flag == True:
            logic.add_new_2(board)
        else:
            print("Invalid Move")

    # repeat above logic for other moves
        
    # down move for "s" input
    elif command.lower() == "s":
        board, flag = logic.move_down(board)
        if status == "CONTINUE" and flag == True:
            logic.add_new_2(board)
        else:
            print("Invalid Move")

    # left move for "a" input
    elif command.lower() == "a":
        board, flag = logic.move_left(board)
        if status == "CONTINUE" and flag == True:
            logic.add_new_2(board)
        else:
            print("Invalid Move")

    # right move for "d" input
    elif command.lower() == "d":
        board, flag = logic.move_right(board)
        if status == "CONTINUE" and flag == True:
            logic.add_new_2(board)
        else:
            print("Invalid Move")

    else:
        print("Invalid Key Pressed")

    # print the board after each move
    for r in range(4):
        print(board[r])