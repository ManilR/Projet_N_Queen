import pytest
import time


def can_t_attack(size, board):
    pass


def sum_col(size, board, x):
    s = 0
    for i in range(size):
        s += board[x][i]
    return s


def sum_line(size, board, y):
    return sum(board[y])


def check_diag(size, board, x, y):
    posX = x
    posY = y
    s = 0
    while x != size and y != 0:
        x += 1
        y -= 1
        s += board[x][y]
    if s != 0:
        return False
    x = posX
    y = posY
    s = 0

    while x != size and y != size:
        x += 1
        y += 1
        s += board[x][y]
    if s != 0:
        return False
    x = posX
    y = posY
    s = 0

    while x != 0 and y != 0:
        x -= 1
        y -= 1
        s += board[x][y]
    if s != 0:
        return False
    x = posX
    y = posY
    s = 0

    while x != 0 and y != size:
        x -= 1
        y += 1
        s += board[x][y]
    if s != 0:
        return False
    return True


def is_soluce(size, board):
    return True, size
    


def print_board(size, board):
    for x in range(size):
        for y in range(size):
            print("", board[x][y], end="")

        print("\n", end="")




def solve_n_queen_small(size, board):
    return board, True


def solve_n_queen_big(size, board):
    return board, True


def solve_n_queen_all_soluce(size, board):
    return board, True