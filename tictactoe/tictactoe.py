"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0
    initialBoard = initial_state()
    for row in board:
        for cell in row:
            if cell == X:
                xCounter += 1
            elif cell == O:
                oCounter += 1

    if board == initialBoard:
        return X
    elif xCounter > oCounter:
        return O
    elif xCounter == oCounter:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    previousBoard = copy.deepcopy(board)

    #checking if the move is legal
    i = action[0]
    j = action[1]
    if previousBoard[i][j] != EMPTY:
        raise ValueError
    else:
        newBoard = copy.deepcopy(board)
        if player(board) == X:
            newBoard[i][j] = X
        elif player(board) == O:
            newBoard[i][j] = O
        return newBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter = 0
    for row in board:
        for cel in row:
            if cel != EMPTY:
                counter += 1

    if counter == 9:
        return True
    elif utility(board) == 1 or utility(board) == -1:
        return True
    elif utility(board) == 0:
        return False
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    index = [0,1,2]
    for num in index:
        if board[num][0] == board[num][1] == board[num][2]:
            if board[num][0] == X:
                return 1
            elif board[num][0] == O:
                return -1
            elif board[num][0] == EMPTY:
                continue

        elif board[0][num] == board[1][num] == board[2][num]:
            if board[0][num] == X:
                return 1
            elif board[0][num] == O:
                return -1
            elif board[0][num] == EMPTY:
                continue

        elif board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] == X:
                return 1
            elif board[1][1] == O:
                return -1
            elif board[1][1] == EMPTY:
                continue

    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    First, it needs to know who's playing
    """
    currentPlayer = player(board)
    if terminal(board):
        return None

    if currentPlayer == X:
        value = maxValue(board)
        move = valueMove(value, board)
        return move

    elif currentPlayer == O:
        value = minValue(board)
        move = valueMove(value, board)
        return move


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

def valueMove(value,board):
    currentPlayer = player(board)
    bestMove = None
    if currentPlayer == X:
        v = -math.inf
        for action in actions(board):
            if value == max(v, minValue(result(board, action))):
                bestMove = action

    elif currentPlayer == O:
        v = math.inf
        for action in actions(board):
            if value == min(v, maxValue(result(board, action))):
                bestMove = action
    return bestMove