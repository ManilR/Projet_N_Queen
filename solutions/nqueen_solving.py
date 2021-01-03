import pytest
import time


# Fonctions Utilitaires

def can_t_attack(size, board):
    for x in range(size):
        for y in range(size):
            if board[x][y] == 1 and not pos_can_t_attack(size, board, x, y):
                return False
    return True


def pos_can_t_attack(size, board, x, y):
    for i in range(size):  # check des lignes
        if board[x][i] == 1 and not i == y:
            return False
    for i in range(size):  # check des colonnes
        if board[i][y] == 1 and not i == x:
            return False

    for i in range(size):  # pour toutes les lignes
        for j in range(size):  # pour toutes les colonnes
            if board[i][j] == 1 and not i == x and not j == y:
                if abs(i - x) == abs(j - y):  # check diagonal
                    return False
    return True


def is_soluce(size, board):
    boardSum = 0
    for x in range(size):
        for y in range(size):
            boardSum += board[x][y]
    if can_t_attack(size, board) and boardSum == size:
        return True, boardSum
    return False, boardSum


def print_board(size, board):
    for x in range(size):
        for y in range(size):
            print("", board[x][y], end="")

        print("\n", end="")


# Algo 1 : la naïveté

def solve_n_queen_small(size, board):
    for y in range(size):  # pour toutes les lignes
        for x in range(size):  # pour toutes les colonnes
            if board[y][x] == 0:
                if pos_can_t_attack(size, board, y, x):
                    board[y][x] = 1
                    solve_n_queen_small(size, board)
                    if sum(sum(a) for a in board) == size:
                        return board, True
                    board[y][x] = 0
    solved, boardSum = is_soluce(size, board)
    if solved:
        return board, True
    else:
        return board, False


# Algo 2 :  le meilleur

def solve_n_queen_big(size, board):
    array = [0] * size
    k = 0
    if size % 6 == 2:
        for i in range(2, size + 1, 2):
            array[k] = i - 1
            k += 1

        array[k] = 3 - 1
        k += 1
        array[k] = 1 - 1
        k += 1

        for i in range(7, size + 1, 2):
            array[k] = i - 1
            k += 1

        array[k] = 5 - 1

    elif size % 6 == 3:
        array[k] = 4 - 1
        k += 1
        for i in range(6, size + 1, 2):
            array[k] = i - 1
            k += 1

        array[k] = 2 - 1
        k += 1
        for i in range(5, size + 1, 2):
            array[k] = i - 1
            k += 1

        array[k] = 1 - 1
        k += 1
        array[k] = 3 - 1

    else:
        for i in range(2, size + 1, 2):
            array[k] = i - 1
            k += 1

        for i in range(1, size + 1, 2):
            array[k] = i - 1
            k += 1

    for i in range(size):
        board[array[i]][i] = 1

    return board, True


# Algo 3 : Toutes les combinaisons

def solve_n_queen_all_soluce(size, board):
    old_array_boards = queens_problem(size)
    new_array_boards = []

    for board in old_array_boards:
        new_board = [[0 for x in range(size)] for y in range(size)]
        for i in range(size):
            new_board[board[i]][i] = 1
        new_array_boards.append(new_board)

    return new_array_boards


def queens_problem(size):
    array_solutions = [[]]
    for row in range(size):
        array_solutions = add_one_queen(row, size, array_solutions)
    return array_solutions


def add_one_queen(new_row, size, prev_solutions):
    return [solution + [new_column]
            for solution in prev_solutions
            for new_column in range(size)
            if no_conflict_all_soluce(new_row, new_column, solution)]


def no_conflict_all_soluce(new_row, new_col, solution):
    if new_col in solution:
        return False
    for row, col in enumerate(solution):
        if row + col == new_row + new_col or row - col == new_row - new_col:
            return False
    return True
