
import copy
import math


def scanVic(board):  #This function returns a tuple which consists of the boolean value, indicating if the game has ended, as well as a
                     # sign of a winner, a string "draw" in case of a draw, or None in case the game is still active
    moves_ = get_moves(board)
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return (True, board[i][0])
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return (True, board[0][i])
    if board[1][1] == board[0][0] == board[2][2] and board[1][1] != " ":
            return (True, board[1][1])
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return (True, board[0][2]) 
    
    if len(moves_) == 0:
        return (True, "draw")
    else:
        return (False, None)
        

def get_moves(board):  #Returns a list of available moves
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i,j))
    return moves



def compMove(board):   #Returns a best move as a tuple with i,j coordinates 
    grid_copy = copy.deepcopy(board)
    empty = get_moves(grid_copy)
    best_score = -math.inf
    best_move = (-1, -1)  # Initialize with valid coordinates
    for i, j in empty:
        grid_copy[i][j] = "O"
        score = minimax(False, grid_copy)
        if score > best_score:
            best_score = score
            best_move = (i, j)
        grid_copy[i][j] = " "  # Reset the cell to empty
    return best_move

def minimax(aiMove, board):  #Returns a "value" of the move for which it was called
    state, sign = scanVic(board)
    if state and sign == "X":
        return -1
    elif state and sign == "O":
        return 1
    elif state and sign == "draw":
        return 0
    
    scores = []

    empty = get_moves(board)

    for i, j in empty:
        if aiMove:
            board[i][j] = "O"
        else: 
            board[i][j] = "X"
        scores.append(minimax(not aiMove, board))
        board[i][j] = " "
    if aiMove:
        return max(scores)
    else:
        return min(scores)

