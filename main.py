
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

def choose_hole():
    hole = int(input("Choose hole (1-12):"))
    while hole < 1 or hole > 12:
        hole = int(input("Wrong Number, Choose hole (1-12):"))
    if hole > 6:
        hole = hole + 1
    while board[hole] == 0:
        hole = int(input("Hole is Empty, Choose another hole"))
        while hole < 1 or hole > 13:
            hole = int(input("Wrong Number, Choose hole (1-12):"))
        if hole > 6:
            hole = hole + 1
    return hole


board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
print_board(board)

playerTurn = True
while board[0]+board[7] < 48:
    if playerTurn:
        print("\nPlayer 1 turn")
    else:
        print("\nPlayer 2 turn")
    hole = choose_hole()
    playerTurn = not playerTurn







