
import random as r

k = 3 # square board grid size

board = ["_" for _ in range(1, k**2 + 1)]

def board_print(board): # prints k x k grid
    for number in [n*k for n in range(1, k + 1)]:
        for position in board[number-k:number]:
            print(position, end=" ")
        print()

winning_conditions = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9), # horizontal
    (1, 4, 7), (2, 5, 8), (3, 6, 9), # vertical
    (1, 5, 9), (3, 5, 7) # diagonal
]

def win_check(board, player):
    for condition in winning_conditions:
        if all(board[position-1] == player for position in condition):
            return True
    return False


def pick_who_starts():
    who_plays = r.randint(0, 1)
    if who_plays == 0:
        return "CPU"
    return "Player"

def CPU_play_random(board, player):
    position = r.randint(0, 8)
    if board[position] != "_":
        return CPU_play_random(board, player)
    board[position] = player
    if win_check(board, player):
        return "Win"
    return None

def Player_play(board, player):
    play = input(f"Where will you place your {player}? ")
    try:
        play = int(play)
    except:
        print("Invalid position.")
        return Player_play(board, player)
    if not(board[play-1] != "_"):
        board[play-1] = player
        if win_check(board, player):
            return "Win"
        return None
    else:
        print("Invalid position.")
        return Player_play(board, player)

# make minimax later!!!!

first = pick_who_starts()


if first == "Player":
    while True:
        print("\nYour Play:")
        P1 = Player_play(board, "X")
        board_print(board)
        if P1 == "Win":
            print("The human player has won the game.")
            break
        print("\nCPU Play:")
        P2 = CPU_play_random(board, "O")
        board_print(board)
        if P2 == "Win":
            print("The CPU player has won the game.")
            break

else:
    while True:
        print("\nCPU Play:")
        P1 = CPU_play_random(board, "X")
        board_print(board)
        if P1 == "Win":
            print("The CPU player has won the game.")
            break
        print("\nYour Play:")
        P2 = Player_play(board, "O")
        board_print(board)
        if P2 == "Win":
            print("The human player has won the game.")
            break


# FOR LATER: try to make the winning conditions for a k x k board.