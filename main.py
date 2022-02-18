import time


def print_board(board):
    print("Player2      6         5         4         3         2         1      Player1")
    print("|-----|   |-----|   |-----|   |-----|   |-----|   |-----|   |-----|   |-----|")
    print("|     |   |     |   |     |   |     |   |     |   |     |   |     |   |     |")
    print("|     |   | ", board[6], " |   | ", board[5], " |   | ", board[4], " |   | ", board[3], " |   | ", board[2],
          " |   | ", board[1], " |   |     |")
    print("|     |   |     |   |     |   |     |   |     |   |     |   |     |   |     |")
    print("| ", board[7], " |   -------   -------   -------   -------   -------   -------   | ", board[0], " |")
    print("|     |   |     |   |     |   |     |   |     |   |     |   |     |   |     |")
    print("|     |   | ", board[8], " |   | ", board[9], " |   | ", board[10], " |   | ", board[11], " |   | ",
          board[12], " |   | ", board[13], " |   |     |")
    print("|     |   |     |   |     |   |     |   |     |   |     |   |     |   |     |")
    print("|-----|   |-----|   |-----|   |-----|   |-----|   |-----|   |-----|   |-----|")
    print("Player2      7         8         9        10        11        12      Player1")
    print("_____________________________________________________________________________")

def choose_hole(board):
    hole = int(input("Choose hole (1-12):"))
    while hole < 1 or hole > 12:
        hole = int(input("Wrong Number, Choose hole (1-12):"))
    if hole > 6:
        hole = hole + 1
    while board[hole] == 0:
        hole = int(input("Hole is Empty, Choose another hole (1-12):"))
        while hole < 1 or hole > 13:
            hole = int(input("Wrong Number, Choose hole (1-12):"))
        if hole > 6:
            hole = hole + 1
    return hole

def play_turn(board, hole):
    num = board[hole]
    newHole = hole+1
    if newHole == 14:
        newHole = 0
    board[hole] = 0
    for i in range(num):
        board[newHole] = board[newHole] + 1
        newHole = newHole + 1
        if newHole == 14:
            newHole = 0
    print("\n")
    print_board(board)
    time.sleep(0.5)
    return newHole - 1

def board_init():
    board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
    print_board(board)
    return board

def wins_check(board):
    if board[0] > board[7]:
        print("\n*=*=*=*=*=* PLAYER 1 WINS !! *=*=*=*=*=*\n")
    elif board[0] == board[7]:
        print("\n*=*=*=*=*=* IT'S A DRAW *=*=*=*=*=*\n")
    else:
        print("\n*=*=*=*=*=* PLAYER 2 WINS !! *=*=*=*=*=*\n")

def game_play(board):
    playerTurn = True
    while board[0] + board[7] < 48:
        if playerTurn:
            print("Player 1 turn")
        else:
            print("Player 2 turn")
        hole = choose_hole(board)
        while board[hole] != 1 and hole != 0 and hole != 7:
            hole = play_turn(board, hole)
        playerTurn = not playerTurn
    wins_check(board)


game_play(board_init())







