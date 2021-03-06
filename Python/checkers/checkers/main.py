# I just use tridecimal counting or something because I was to lazy to figure out what 10, 11, and 12's number should be
board = [[" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
         [" | ", "   ", "(A)", "   ", "(B)", "   ", "(C)", "   ", "(D)", " | "],  # # # # # # # # # #
         [" | ", "(E)", "   ", "(F)", "   ", "(G)", "   ", "(H)", "   ", " | "],  # Player 1  Pieces
         [" | ", "   ", "(I)", "   ", "(J)", "   ", "(K)", "   ", "(L)", " | "],  #
         [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
         [" | ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " | "],
         [" | ", "[A]", "   ", "[B]", "   ", "[C]", "   ", "[D]", "   ", " | "],  # # # # # # # # # #
         [" | ", "   ", "[E]", "   ", "[F]", "   ", "[G]", "   ", "[H]", " | "],  # Player 2 Pieces
         [" | ", "[I]", "   ", "[J]", "   ", "[K]", "   ", "[L]", "   ", " | "],  #
         [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]]
boardSize = [10, 10]

# First 12 positions are player 1's pieces and last 12 positions are player 2's pieces
# In sub arrays, positions are stored as [y, x]
piecesPos = [[1, 2], [1, 4], [1, 6], [1, 8],  # # # # # # # # # #
             [2, 1], [2, 3], [2, 5], [2, 7],  # Player 1 Pieces
             [3, 2], [3, 4], [3, 6], [3, 8],  #

             [6, 1], [6, 3], [6, 5], [6, 7],  # # # # # # # # # #
             [7, 2], [7, 4], [7, 6], [7, 8],  # Player 2 Pieces
             [8, 1], [8, 5], [8, 5], [8, 7]]  #


# r - row | c - collum
def draw():
    r = 0
    c = 0

    global board
    global boardSize
    global piecesPos


    while r <= boardSize[0] - 1:
        while c <= boardSize[1] - 1:

            print(board[r][c], end="")
            c += 1
        c = 0
        r += 1
        print(end="\n")


def askMove():
    playerTurn = "1"

    # move[0] = piece, move[1] = dir, who's move it was
    move = ["", "", playerTurn]

    if playerTurn == "1":
        playerInput = input("Player 1, what piece would you like to move and where (Format: \"<piece char> <dir (UL, UR, DL, DR)>\")?\n"
                            "If you can't move type \"forfeit\". - ")

        move[0] = playerInput[0]
        move[1] = playerInput[2] + playerInput[3]
        playerTurn = "2"


    else:
        playerInput = input("Player 2, what piece would you like to move and where (Format: \"<piece char> <dir (UL, UR, DL, DR)>\")?\n"
                            "If you can't move type \"forfeit\". - ")

        move[0] = playerInput[0]
        move[1] = playerInput[2] + playerInput[3]
        playerTurn = "1"

    return move


# Checks if the piece can move in the desired direction

def canMoveCheck(piece, dir, player):
    global piecesPos

    global boardSize

    piecesDict = {
        "A": 0,

        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
    }
    
    dirDict = {
        "UL": [-1, -1],
        "UR": [-1, 1],
        "DL": [1, -1],
        "DR": [1, 1]
    }

    if player == "1":
        nextPos = [0, 0]
        nextPos[0] = piecesPos[piecesDict[piece]][0] + dirDict[dir][0]
        nextPos[1] = piecesPos[piecesDict[piece]][1] + dirDict[dir][1]

    if player == "2":
        nextPos = [0, 0]
        nextPos[0] = piecesPos[piecesDict[piece] + 12][0] + dirDict[dir][0]
        nextPos[1] = piecesPos[piecesDict[piece] + 12][1] + dirDict[dir][1] 

    # Checks if the next spot is off the board
    if nextPos > boardSize or nextPos < 0:

        print("Your desired move is goes off the board. Please try again.")
        return False

    # Checks if the next spot on the board is occupied
    elif board[nextPos[0]][nextPos[1]] == "   ":
        return True

    # Checks if the spot after that is off the board

    elif nextPos + dir > boardSize or nextPos + dir < 0:
        print("You cannot move in that direction. Please try again.")
        return False

    # If it is it checks the spot after that

    elif board[nextPos[0] + dir][nextPos[1] + dir] == "   ":

        return True

    # If that is it tells the player it can't move there
    else:
        print("You cannot move in that direction. Please try again.")
        return False

def move(piece, dir, player):
    global piecesPos
    global board

    piecesDict = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
    }
    
    dirDict = {
        "UL": [-1, -1],
        "UR": [-1, 1],
        "DL": [1, -1],
        "DR": [1, 1]
    }

    if player == "1":
        currentPos = [0, 0]
        currentPos[0] = piecesPos[piecesDict[piece]][0]
        currentPos[1] = piecesPos[piecesDict[piece]][1]

        nextPos = [0, 0]
        nextPos[0] = piecesPos[piecesDict[piece]][0] + dirDict[dir][0]
        nextPos[1] = piecesPos[piecesDict[piece]][1] + dirDict[dir][1]

    if player == "2":
        currentPos = [0, 0]
        currentPos[0] = piecesPos[piecesDict[piece] + 12][0]
        currentPos[1] = piecesPos[piecesDict[piece] + 12][1]

        nextPos = [0, 0]
        nextPos[0] = piecesPos[piecesDict[piece] + 12][0] + dirDict[dir][0]
        nextPos[1] = piecesPos[piecesDict[piece] + 12][1] + dirDict[dir][1]
    
    board[currentPos[0]][currentPos[1]] = "   "
    
    if player == "1":
        board[nextPos[0]][nextPos[1]] = "(" + piece + ")"
        piecesPos[piecesDict[piece]] = nextPos
    else:
        board[nextPos[0]][nextPos[1]] = "[" + piece + "]"
        piecesPos[piecesDict[piece]] = nextPos
